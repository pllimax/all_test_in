#!/bin/bash

# 用法:
#   自动收集: ./collect_metrics.sh                              (收集今天及前3天数据)
#   指定日期: ./collect_metrics.sh 20260716
#   多个日期: ./collect_metrics.sh 20260716 20260717 20260718   (按先后顺序轮流执行)
#   自定义配置: SRC_BASE=/custom/path GIT_REPO=git@github.com:user/repo.git ./collect_metrics.sh 20260716
#   使用配置文件: ./collect_metrics.sh 20260716 --config /path/to/config.conf
#   命令行覆盖: ./collect_metrics.sh --src-base /custom/path --git-repo git@github.com:user/repo.git 20260716
#   分支模式:   ./collect_metrics.sh --branch pllimax            (按 CI 目录名 {branch}-{date}-{run_id}-{attempt} 归类)
# 从指定目录下各子目录中收集 bench_serving_metrics.txt（性能）与 eval_log.log（精度）文件。

# 新 CI 目录结构:
#   SRC_BASE/{branch}-{date}-{run_id}-{attempt}/{workflow}/{type}/{suite}-{timestamp}/{tc_name}/bench_serving_metrics.txt
#   SRC_BASE/{branch}-{date}-{run_id}-{attempt}/{workflow}/{type}/{suite}-{timestamp}/{tc_name}/[eval_ts]/logs/eval_log.log
# 同时兼容旧结构（按日期目录存放，{tc_name}-{timestamp}）。

set -e

# ============================================================
# 配置项：优先使用环境变量，提供默认值
# ============================================================
SRC_BASE="${SRC_BASE:-/data/ascend-ci-share-pkking-sglang/tests/output}"
# 默认使用 HTTPS（与 prometheus_exporter.py 默认一致，公开仓可直接 clone）；
# 私有仓推送请通过 GIT_REPO 环境变量或 --git-repo 指定带凭据地址（如 git@github.com:org/repo.git）
GIT_REPO="${GIT_REPO:-https://github.com/pllimax/all_test_in.git}"
GIT_TARGET_PATH="${GIT_TARGET_PATH:-upload_performance_result/metrics/sglang}"
GIT_LOCAL_DIR="${GIT_LOCAL_DIR:-}"
BRANCH="${BRANCH:-}"

# ============================================================
# 参数解析
# ============================================================
SPECIFIED_DATES=()

while [[ $# -gt 0 ]]; do
    case $1 in
        --config)
            CONFIG_FILE="$2"
            shift 2
            ;;
        --src-base)
            SRC_BASE="$2"
            shift 2
            ;;
        --git-repo)
            GIT_REPO="$2"
            shift 2
            ;;
        --git-target-path)
            GIT_TARGET_PATH="$2"
            shift 2
            ;;
        --branch)
            BRANCH="$2"
            shift 2
            ;;
        --help|-h)
            echo "用法: $0 [选项] [日期...]"
            echo ""
            echo "参数:"
            echo "  日期...               收集数据的日期，格式如 20260716"
            echo "                        可指定多个日期，按先后顺序轮流执行"
            echo "                        不指定时自动收集今天及前3天数据"
            echo "                        （分支模式下不指定日期则只收集一次，避免重复）"
            echo ""
            echo "选项:"
            echo "  --config FILE         配置文件路径"
            echo "  --src-base PATH       源目录基础路径（不包含日期部分）"
            echo "  --git-repo REPO       Git仓库地址"
            echo "  --git-target-path PATH Git仓库中的目标路径"
            echo "  --branch NAME         按前缀筛选收集任务结果"
            echo "                        如 --branch pllimax 匹配所有以 pllimax 开头的目录"
            echo "                        (即 pllimax 仓下所有分支的 CI 任务)"
            echo "                        分支模式下结果按 CI 目录名({branch}-{date}-{run_id}-{attempt})/workflow目录 存放，不使用日期"
            echo "  --help, -h            显示此帮助信息"
            echo ""
            echo "收集内容:"
            echo "  1) 性能结果: bench_serving_metrics.txt（存为 {用例名}__{日期}.txt）"
            echo "  2) 精度结果: eval_log.log（存为 {用例名}__{日期}.log，目录加 /eval）"
            echo "  兼容新旧 CI 目录结构（新结构含 suite/timestamp，旧结构按日期目录）"
            echo ""
            echo "环境变量:"
            echo "  SRC_BASE              源目录基础路径"
            echo "  GIT_REPO              Git仓库地址"
            echo "  GIT_TARGET_PATH       Git仓库中的目标路径"
            echo "  GIT_LOCAL_DIR         Git本地临时目录"
            echo "  BRANCH                仅收集指定分支"
            echo ""
            echo "示例:"
            echo "  $0                        # 自动收集今天及前3天"
            echo "  $0 20260716               # 单个日期"
            echo "  $0 20260716 20260717 20260718   # 多个日期轮流执行"
            echo "  $0 --branch pllimax                      # 前缀匹配，收集 pllimax 仓所有分支任务"
            echo "  $0 --branch pllimax 20260727             # 前缀匹配 + 日期过滤"
            echo "  SRC_BASE=/custom/path $0 20260716"
            echo "  $0 --src-base /custom/path --git-repo git@github.com:user/repo.git 20260716"
            echo "  $0 --config my_config.conf 20260716"
            exit 0
            ;;
        -*)
            echo "错误: 未知选项 $1"
            echo "使用 --help 查看帮助信息"
            exit 1
            ;;
        *)
            SPECIFIED_DATES+=("$1")
            shift
            ;;
    esac
done

# 加载配置文件（如果指定）
if [ -n "${CONFIG_FILE:-}" ]; then
    if [ -f "$CONFIG_FILE" ]; then
        source "$CONFIG_FILE"
        echo "已加载配置文件: $CONFIG_FILE"
    else
        echo "错误: 配置文件不存在: $CONFIG_FILE"
        exit 1
    fi
fi

# 自动模式：未指定日期时，收集今天及前3天数据
AUTO_MODE=false
if [ ${#SPECIFIED_DATES[@]} -eq 0 ]; then
    AUTO_MODE=true
    TODAY=$(date +%Y%m%d)
    DATES=()
    for i in 0 1 2 3; do
        d=$(date -d "$TODAY - $i days" +%Y%m%d 2>/dev/null)
        if [ -n "$d" ]; then
            DATES+=("$d")
        fi
    done
    # 升序排列
    IFS=$'\n' DATES=($(sort <<<"${DATES[*]}")); unset IFS
    echo "自动模式: 收集 ${DATES[0]} ~ ${DATES[-1]} 共 ${#DATES[@]} 天数据"
else
    DATES=("${SPECIFIED_DATES[@]}")
fi

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# 设置 Git 本地目录默认值（依赖 SCRIPT_DIR）
if [ -z "$GIT_LOCAL_DIR" ]; then
    GIT_LOCAL_DIR="${SCRIPT_DIR}/.all_test_in_repo"
fi

# 本次收集文件清单：仅上传本次实际收集的用例文件，
# 避免 CI 机器上旧的/未收集的文件覆盖 git 仓库中他人刚提交的新内容。
# 清单放在系统临时目录，避免落入仓库目录被 git add 误提交。
UPLOAD_LIST="${TMPDIR:-/tmp}/upload_list_$$"
: > "${UPLOAD_LIST}"
trap 'rm -f "${UPLOAD_LIST}"' EXIT

# 提醒：脚本所在 checkout 若落后于远端，用旧代码/旧数据运行会有回退仓库新提交的风险
if git -C "${SCRIPT_DIR}" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    repo_root=$(git -C "${SCRIPT_DIR}" rev-parse --show-toplevel 2>/dev/null || true)
    if [ -n "${repo_root}" ]; then
        local_head=$(git -C "${repo_root}" rev-parse HEAD 2>/dev/null || true)
        remote_head=$(git -C "${repo_root}" ls-remote origin HEAD 2>/dev/null | awk '{print $1}')
        if [ -n "${local_head}" ] && [ -n "${remote_head}" ] && [ "${local_head}" != "${remote_head}" ]; then
            echo "警告: 脚本所在仓库落后于远端 (本地 ${local_head:0:8} vs 远端 ${remote_head:0:8})。"
            echo "      建议先在 CI 上同步最新代码再执行本脚本，否则可能用旧逻辑/旧数据覆盖仓库中的新提交。"
        fi
    fi
fi

# ============================================================
# 搜索根目录：支持按分支前缀筛选
# 前缀匹配，如 --branch pllimax 可匹配 pllimax 下所有分支目录
# 分支模式下排除仅以日期命名的旧结构目录（YYYYMMDD）
# ============================================================
if [ -n "${BRANCH:-}" ]; then
    SEARCH_ROOTS=()
    for d in "${SRC_BASE}"/"${BRANCH}"*; do
        if [ -d "$d" ]; then
            base_name=$(basename "$d")
            # 仅收集 CI 运行目录（如 {branch}-{date}-{run_id}-{attempt}），
            # 跳过仅以日期为文件夹名的目录（旧结构按日期存放的结果）
            if ! echo "${base_name}" | grep -qE '^[0-9]{8}$'; then
                SEARCH_ROOTS+=("$d")
            fi
        fi
    done
    if [ ${#SEARCH_ROOTS[@]} -eq 0 ]; then
        echo "错误: 未找到匹配分支前缀 ${BRANCH} 的任务目录 (${SRC_BASE}/${BRANCH}*，且排除日期目录)"
        exit 1
    fi
    echo "分支筛选: ${BRANCH} (前缀匹配, 排除日期目录) → 匹配 ${#SEARCH_ROOTS[@]} 个任务目录"
else
    SEARCH_ROOTS=("${SRC_BASE}")
fi

# ============================================================
# 分支模式：取消按日期循环收集
# 分支目录名已含任务创建日期（{branch}-{date}-{run_id}-{attempt}），
# 自动日期循环（今天及前3天）会导致同一批结果被重复收集 4 次。
# 未显式指定日期时，分支模式仅收集一次，文件名以今天日期作标记。
# ============================================================
if [ -n "${BRANCH:-}" ] && [ ${#SPECIFIED_DATES[@]} -eq 0 ]; then
    AUTO_MODE=false
    DATES=("$(date +%Y%m%d)")
    echo "分支模式: 取消自动日期循环，仅收集一次（文件名日期标记: ${DATES[0]}）"
fi

# ============================================================
# 配置验证
# ============================================================
echo "========== 配置信息 =========="
echo "源目录基础路径: ${SRC_BASE}"
if [ -n "${BRANCH:-}" ]; then
    echo "分支筛选:       ${BRANCH} (${#SEARCH_ROOTS[@]} 个任务目录)"
fi
echo "Git仓库:        ${GIT_REPO}"
echo "Git目标路径:    ${GIT_TARGET_PATH}"
if [ "$AUTO_MODE" = true ]; then
    echo "日期范围:       ${DATES[0]} ~ ${DATES[-1]} (共 ${#DATES[@]} 天)"
else
    echo "日期列表:       ${DATES[*]} (共 ${#DATES[@]} 个)"
fi
echo "=============================="
echo ""

# 全局计数
TOTAL_PERF_COUNT=0
TOTAL_EVAL_COUNT=0

# ============================================================
# 公共工具函数
# ============================================================

# 获取文件实际修改时间（秒级时间戳），兼容 Linux/macOS。
# 失败时输出空字符串，调用方据此跳过。
_file_mtime() {
    stat -c '%Y' "$1" 2>/dev/null || stat -f '%m' "$1" 2>/dev/null
}

# 将秒级时间戳格式化为 YYYYmmdd（日期模式归类用）。
# 失败时输出空字符串。
_mtime_date() {
    date -d "@$1" +%Y%m%d 2>/dev/null || date -r "$1" +%Y%m%d 2>/dev/null
}

# 将秒级时间戳格式化为 'YYYY-MM-DD HH:MM:SS'（文件末尾元信息用）。
_mtime_human() {
    date -d "@$1" '+%Y-%m-%d %H:%M:%S' 2>/dev/null || date -r "$1" '+%Y-%m-%d %H:%M:%S' 2>/dev/null
}

# 剥离可能的 CI 时间戳后缀（兼容旧结构 {tc_name}-{timestamp}），保留干净的用例名。
_strip_ci_ts() {
    echo "$1" | sed 's/-[0-9]\{6\}$//'
}

# 从源文件绝对路径中提取 CI 顶层目录名与 workflow 目录名。
# 新 CI 结构: SRC_BASE/{branch}-{date}-{run_id}-{attempt}/{workflow}/{type}/...
# 输出格式: "{ci_dir_name}|{wf_type}"
_ci_top_level() {
    local file="$1"
    local rel="${file#${SRC_BASE}/}"
    local ci_dir_name="${rel%%/*}"
    local tmp="${rel#*/}"
    local wf_type="${tmp%%/*}"
    echo "${ci_dir_name}|${wf_type}"
}

# 计算目标存放目录：
#   分支模式（--branch）→ 按 CI 顶层目录名（{branch}-{date}-{run_id}-{attempt}）保存，
#                         并在其中按 workflow 目录（如 Full_Test_NPU）区分
#   否则 → 按文件实际修改日期保存
# 参数: $1=源文件绝对路径  $2=mtime 秒级时间戳  $3=子目录（如 eval/，可空）
# 输出: 目标目录绝对路径；日期模式无法转换日期时输出空字符串
_collect_target_dir() {
    local file="$1" mtime="$2" subdir="$3"
    if [ -n "${BRANCH:-}" ]; then
        local top
        top=$(_ci_top_level "${file}")
        echo "${SCRIPT_DIR}/${top%%|*}/${top#*|}/${subdir}"
    else
        local actual_date
        actual_date=$(_mtime_date "${mtime}")
        [ -z "${actual_date}" ] && echo "" && return 1
        echo "${SCRIPT_DIR}/${actual_date}/${subdir}"
    fi
}

# 遍历每个日期进行收集
for CURRENT_DATE in "${DATES[@]}"; do
    echo ""
    echo "========== 处理日期: ${CURRENT_DATE} =========="

    # 新 CI 目录结构: SRC_BASE/{branch}-{date}-{run_id}-{attempt}/{workflow}/{type}/{suite}-{timestamp}/{tc_name}/bench_serving_metrics.txt
    # 不再有空目录检查 —— 用 find 递归搜索 SRC_BASE 全树，由 mtime 日期过滤

    echo "源目录: ${SEARCH_ROOTS[*]} (递归搜索，按 mtime 日期过滤: ${CURRENT_DATE})"
    echo "目标: 按文件实际修改时间归类到 SCRIPT_DIR/YYYYmmdd/"
    echo ""

    count=0
    # 递归查找所有 bench_serving_metrics.txt，根据文件实际修改时间归类到对应日期目录
    while IFS= read -r src_file; do
        [ -f "${src_file}" ] || continue

        # 新结构: subdir = {suite}-{timestamp}/{tc_name}，subdir_name 即 {tc_name}
        # 旧结构: subdir = {tc_name}-{timestamp}
        subdir=$(dirname "${src_file}")
        subdir_name=$(basename "${subdir}")
        # 剥离可能的 CI 时间戳后缀（兼容旧结构 {tc_name}-{timestamp}），保留干净的用例名
        subdir_name_clean=$(_strip_ci_ts "${subdir_name}")
        # 新结构: 父目录为 {suite}-{timestamp}，用于日志展示与来源追溯
        suite_dir=$(dirname "${subdir}")
        suite_name=$(basename "${suite_dir}")

        # 获取文件实际修改时间（秒级时间戳），失败则跳过
        mtime_epoch=$(_file_mtime "${src_file}")
        if [ -z "${mtime_epoch}" ]; then
            echo "[WARN] ${subdir_name}: 无法获取文件修改时间，跳过"
            continue
        fi

        # 非分支模式：仅收集实际修改日期与请求日期一致的文件。
        # 否则 find 会命中全树所有历史文件，导致指定单日收集偏多、
        # 自动模式同一文件被多个日期重复收集。
        if [ -z "${BRANCH:-}" ]; then
            actual_date=$(_mtime_date "${mtime_epoch}")
            if [ "${actual_date}" != "${CURRENT_DATE}" ]; then
                continue
            fi
        fi

        # 计算目标目录（分支模式按 CI 目录，否则按实际修改日期）
        PERF_TARGET_DIR=$(_collect_target_dir "${src_file}" "${mtime_epoch}" "")
        if [ -z "${PERF_TARGET_DIR}" ]; then
            echo "[WARN] ${subdir_name}: 无法转换修改时间，跳过"
            continue
        fi
        mkdir -p "${PERF_TARGET_DIR}"

        dst_file="${PERF_TARGET_DIR}/${subdir_name_clean}__${CURRENT_DATE}.txt"
        cp "${src_file}" "${dst_file}"

        # 在文件末尾追加原始修改时间描述
        mtime_human=$(_mtime_human "${mtime_epoch}")
        {
            echo ""
            echo "# [collect_metrics] 文件原始修改时间: ${mtime_human}"
            echo "# [collect_metrics] 源目录日期: ${CURRENT_DATE}"
            echo "# [collect_metrics] CI运行目录: ${suite_name}/${subdir_name}"
        } >> "${dst_file}"

        # 记录本次收集的文件（上传时仅推送清单内文件，避免回退仓库新提交）
        echo "${dst_file}" >> "${UPLOAD_LIST}"

        if [ -n "${BRANCH:-}" ]; then
            top_info=$(_ci_top_level "${src_file}")
            echo "[OK] ${subdir_name_clean} (suite: ${suite_name}, 源目录: ${top_info%%|*}/${top_info#*|}, 源目录日期: ${CURRENT_DATE})"
        else
            echo "[OK] ${subdir_name_clean} (suite: ${suite_name}, 源目录日期: ${CURRENT_DATE}, 实际修改日期: $(_mtime_date "${mtime_epoch}"))"
        fi
        count=$((count + 1))
    done < <(find "${SEARCH_ROOTS[@]}" -type f -name 'bench_serving_metrics.txt' -path '*/perf/*')

    echo ""
    if [ -n "${BRANCH:-}" ]; then
        echo "完成: 共收集 ${count} 个性能测试文件（按 ${SCRIPT_DIR}/{目录名}/{workflow目录}/ 归类）"
    else
        echo "完成: 共收集 ${count} 个性能测试文件（按实际修改时间归类）"
    fi
    TOTAL_PERF_COUNT=$((TOTAL_PERF_COUNT + count))

    # ============================================================
    # 收集精度测试结果 (eval_log.log)
    # 新 CI 结构: SRC_BASE/{branch}-{date}-{run_id}-{attempt}/{workflow}/{type}/{suite}-{timestamp}/{tc_name}/[eval_ts]/logs/eval_log.log
    # 所有 perf 和 accuracy 类型的 eval 日志都在 SRC_BASE 下统一搜索
    # 存储: 默认 SCRIPT_DIR/实际日期/eval/，分支模式 SCRIPT_DIR/{目录名}/{workflow目录}/eval/
    # 命名: 按"用例名__源日期.log"
    # ============================================================

    eval_count=0
    while IFS= read -r eval_src; do
        [ -f "${eval_src}" ] || continue

        # 新结构路径: .../output/{branch}-{date}-{run_id}-{attempt}/{workflow}/{type}/{suite}-{timestamp}/{tc_name}/[eval_ts]/logs/eval_log.log
        # 注意 CI 中 {suite}-{timestamp}/{tc_name} 下可能还有一层 {eval_ts}（eval 执行时间戳目录）
        logs_dir=$(dirname "${eval_src}")         # .../{eval_ts}/logs 或 .../{tc_name}/logs
        ts_dir=$(dirname "${logs_dir}")           # .../{eval_ts} 或 .../{suite}-{timestamp}/{tc_name}
        ts_name=$(basename "${ts_dir}")           # {eval_ts} 或 {tc_name}
        # 兼容两种结构：ts_name 为 eval_ts（如 20260805_193018）时，再向上一级取 {tc_name}
        if echo "${ts_name}" | grep -qE '^[0-9]{8}_[0-9]{6}$'; then
            ts_dir=$(dirname "${ts_dir}")
            ts_name=$(basename "${ts_dir}")
        fi
        # 剥离可能的 CI 时间戳后缀（兼容旧结构 {tc_name}-{ci_ts}），保留干净的用例名
        ts_name_clean=$(_strip_ci_ts "${ts_name}")
        # 确定 test_type（perf / accuracy）：
        # 新结构: ts_dir 父目录为 {suite}-{timestamp}（带时间戳），再上一级才是 {type}
        # 旧结构: ts_dir 父目录即为 {test_type}
        suite_dir=$(dirname "${ts_dir}")
        suite_name=$(basename "${suite_dir}")
        if echo "${suite_name}" | grep -qE -- '-[0-9]{6}$'; then
            type_dir=$(dirname "${suite_dir}")
            test_type_name=$(basename "${type_dir}")
        else
            test_type_name="${suite_name}"
        fi

        # 获取文件实际修改时间（秒级时间戳），失败则跳过
        mtime_epoch=$(_file_mtime "${eval_src}")
        if [ -z "${mtime_epoch}" ]; then
            echo "[WARN-EVAL] ${test_type_name}__${ts_name}: 无法获取文件修改时间，跳过"
            continue
        fi

        # 非分支模式：仅收集实际修改日期与请求日期一致的文件（与性能收集保持一致）
        if [ -z "${BRANCH:-}" ]; then
            actual_date=$(_mtime_date "${mtime_epoch}")
            if [ "${actual_date}" != "${CURRENT_DATE}" ]; then
                continue
            fi
        fi

        # 计算目标目录（分支模式按 CI 目录 + /eval，否则按实际修改日期 + /eval）
        EVAL_TARGET_DIR=$(_collect_target_dir "${eval_src}" "${mtime_epoch}" "eval")
        if [ -z "${EVAL_TARGET_DIR}" ]; then
            echo "[WARN-EVAL] ${test_type_name}__${ts_name}: 无法转换修改时间，跳过"
            continue
        fi
        mkdir -p "${EVAL_TARGET_DIR}"

        # 命名: {tc_name_clean}__{源目录日期}.log
        eval_dst="${EVAL_TARGET_DIR}/${ts_name_clean}__${CURRENT_DATE}.log"
        # 如果已存在同名文件（来自不同 workflow 目录等），追加序号后缀区分
        if [ -f "${eval_dst}" ]; then
            suffix=1
            while [ -f "${EVAL_TARGET_DIR}/${ts_name_clean}__${CURRENT_DATE}-${suffix}.log" ]; do
                suffix=$((suffix + 1))
            done
            eval_dst="${EVAL_TARGET_DIR}/${ts_name_clean}__${CURRENT_DATE}-${suffix}.log"
        fi
        cp "${eval_src}" "${eval_dst}"

        # 在文件末尾追加原始修改时间描述
        mtime_human=$(_mtime_human "${mtime_epoch}")
        {
            echo ""
            echo "# [collect_metrics] 文件原始修改时间: ${mtime_human}"
        } >> "${eval_dst}"

        # 记录本次收集的文件（上传时仅推送清单内文件，避免回退仓库新提交）
        echo "${eval_dst}" >> "${UPLOAD_LIST}"

        if [ -n "${BRANCH:-}" ]; then
            top_info=$(_ci_top_level "${eval_src}")
            echo "[EVAL] ${ts_name_clean} (源目录: ${top_info%%|*}/${top_info#*|}, 源目录日期: ${CURRENT_DATE})"
        else
            echo "[EVAL] ${ts_name_clean} (源目录日期: ${CURRENT_DATE}, 实际修改日期: $(_mtime_date "${mtime_epoch}"))"
        fi
        eval_count=$((eval_count + 1))
    done < <(find "${SEARCH_ROOTS[@]}" -type f -name 'eval_log.log' -path '*/logs/eval_log.log')

    if [ ${eval_count} -gt 0 ]; then
        echo ""
        if [ -n "${BRANCH:-}" ]; then
            echo "完成: 共收集 ${eval_count} 个精度测试文件（按 ${SCRIPT_DIR}/{目录名}/{workflow目录}/eval/ 归类）"
        else
            echo "完成: 共收集 ${eval_count} 个精度测试文件（按实际修改时间归类）"
        fi
    fi
    TOTAL_EVAL_COUNT=$((TOTAL_EVAL_COUNT + eval_count))
done

# 汇总
echo ""
echo "========== 收集汇总 =========="
echo "性能测试文件: ${TOTAL_PERF_COUNT} 个"
echo "精度测试文件: ${TOTAL_EVAL_COUNT} 个"
echo "=============================="

# ============================================================
# 上传到 Git 仓库
# ============================================================

echo ""
echo "========== 开始上传到 Git =========="

# 克隆或更新仓库
if [ -d "${GIT_LOCAL_DIR}/.git" ]; then
    echo "更新已有仓库..."
    cd "${GIT_LOCAL_DIR}"
    # 先尝试增量更新（fetch + reset）
    if git fetch origin --depth=1 2>/dev/null && \
       git reset --hard origin/main 2>/dev/null; then
        echo "仓库更新成功"
    else
        # 增量更新失败（如远程被 force push 导致历史不相关），重新克隆
        echo "增量更新失败，正在重新克隆仓库..."
        cd /
        rm -rf "${GIT_LOCAL_DIR}"
        git clone --depth=1 "${GIT_REPO}" "${GIT_LOCAL_DIR}"
        echo "重新克隆完成"
    fi
else
    echo "克隆仓库..."
    rm -rf "${GIT_LOCAL_DIR}"
    git clone --depth=1 "${GIT_REPO}" "${GIT_LOCAL_DIR}"
fi

# 确保目标路径存在
mkdir -p "${GIT_LOCAL_DIR}/${GIT_TARGET_PATH}"

# 仅上传本次实际收集的文件（清单驱动）：
# 1) 未在本次收集的旧文件不会推送，避免把 CI 机器上旧内容回退到 git 仓库的新提交上
# 2) 不使用 --delete，避免删除 Git 仓库中已存在但本地 SCRIPT_DIR 缺失的历史数据
#    （如换机器收集、或本地手动清理过某日期目录）
echo "拷贝本次收集的文件到仓库..."
if [ -s "${UPLOAD_LIST}" ]; then
    while IFS= read -r f; do
        [ -f "${f}" ] || continue
        rel="${f#${SCRIPT_DIR}/}"
        case "${rel}" in
            /*) continue ;;  # 不在 SCRIPT_DIR 下（理论不会发生），跳过
        esac
        dst="${GIT_LOCAL_DIR}/${GIT_TARGET_PATH}/${rel}"
        mkdir -p "$(dirname "${dst}")"
        cp -a "${f}" "${dst}"
    done < "${UPLOAD_LIST}"
    rm -f "${UPLOAD_LIST}"
else
    echo "警告: 本次未收集到任何文件，跳过拷贝。"
fi

# 提交并推送
cd "${GIT_LOCAL_DIR}"
git add "${GIT_TARGET_PATH}/"

if git diff --cached --quiet; then
    echo "无变更，跳过提交。"
else
    git commit -m "update metrics data - ${DATES[0]}~${DATES[-1]}"
    git push origin HEAD
    echo "上传成功!"
fi

echo "========== 上传完成 =========="
