#!/bin/bash

# 用法:
#   自动收集: ./collect_metrics.sh                              (收集今天及前3天数据)
#   指定日期: ./collect_metrics.sh 20260716
#   多个日期: ./collect_metrics.sh 20260716 20260717 20260718   (按先后顺序轮流执行)
#   自定义配置: SRC_BASE=/custom/path GIT_REPO=git@github.com:user/repo.git ./collect_metrics.sh 20260716
#   使用配置文件: ./collect_metrics.sh 20260716 --config /path/to/config.conf
#   命令行覆盖: ./collect_metrics.sh --src-base /custom/path --git-repo git@github.com:user/repo.git 20260716
# 从指定目录下各子目录中收集 bench_serving_metrics.txt 文件

set -e

# ============================================================
# 配置项：优先使用环境变量，提供默认值
# ============================================================
SRC_BASE="${SRC_BASE:-/data/ascend-ci-share-pkking-sglang/tests/output}"
GIT_REPO="${GIT_REPO:-git@github.com-pllimax:pllimax/all_test_in.git}"
GIT_TARGET_PATH="${GIT_TARGET_PATH:-upload_performance_result/metrics/sglang}"
GIT_LOCAL_DIR="${GIT_LOCAL_DIR:-}"

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
        --help|-h)
            echo "用法: $0 [选项] [日期...]"
            echo ""
            echo "参数:"
            echo "  日期...               收集数据的日期，格式如 20260716"
            echo "                        可指定多个日期，按先后顺序轮流执行"
            echo "                        不指定时自动收集今天及前3天数据"
            echo ""
            echo "选项:"
            echo "  --config FILE         配置文件路径"
            echo "  --src-base PATH       源目录基础路径（不包含日期部分）"
            echo "  --git-repo REPO       Git仓库地址"
            echo "  --git-target-path PATH Git仓库中的目标路径"
            echo "  --help, -h            显示此帮助信息"
            echo ""
            echo "环境变量:"
            echo "  SRC_BASE              源目录基础路径"
            echo "  GIT_REPO              Git仓库地址"
            echo "  GIT_TARGET_PATH       Git仓库中的目标路径"
            echo "  GIT_LOCAL_DIR         Git本地临时目录"
            echo ""
            echo "示例:"
            echo "  $0                        # 自动收集今天及前3天"
            echo "  $0 20260716               # 单个日期"
            echo "  $0 20260716 20260717 20260718   # 多个日期轮流执行"
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

# ============================================================
# 配置验证
# ============================================================
echo "========== 配置信息 =========="
echo "源目录基础路径: ${SRC_BASE}"
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

# 遍历每个日期进行收集
for CURRENT_DATE in "${DATES[@]}"; do
    echo ""
    echo "========== 处理日期: ${CURRENT_DATE} =========="

    # 新 CI 目录结构: SRC_BASE/{branch}-{run_id}/{workflow_type}/{test_type}/{tc_name}-{timestamp}/bench_serving_metrics.txt
    # 不再有空目录检查 —— 用 find 递归搜索 SRC_BASE 全树，由 mtime 日期过滤

    echo "源目录: ${SRC_BASE} (递归搜索，按 mtime 日期过滤: ${CURRENT_DATE})"
    echo "目标: 按文件实际修改时间归类到 SCRIPT_DIR/YYYYmmdd/"
    echo ""

    count=0
    # 递归查找所有 bench_serving_metrics.txt，根据文件实际修改时间归类到对应日期目录
    while IFS= read -r src_file; do
        [ -f "${src_file}" ] || continue

        subdir=$(dirname "${src_file}")
        subdir_name=$(basename "${subdir}")
        # 新结构: subdir_name = {tc_name}-{timestamp}，如 test_qwen3_8b-093000
        # 剥离 CI 时间戳后缀，保留干净的用例名
        subdir_name_clean=$(echo "${subdir_name}" | sed 's/-[0-9]\{6\}$//')

        # 获取文件实际修改时间（秒级时间戳），兼容 Linux/macOS
        mtime_epoch=$(stat -c '%Y' "${src_file}" 2>/dev/null || stat -f '%m' "${src_file}" 2>/dev/null)
        if [ -z "${mtime_epoch}" ]; then
            echo "[WARN] ${subdir_name}: 无法获取文件修改时间，跳过"
            continue
        fi

        actual_date=$(date -d "@${mtime_epoch}" +%Y%m%d 2>/dev/null || date -r "${mtime_epoch}" +%Y%m%d 2>/dev/null)
        if [ -z "${actual_date}" ]; then
            echo "[WARN] ${subdir_name}: 无法转换修改时间，跳过"
            continue
        fi

        PERF_TARGET_DIR="${SCRIPT_DIR}/${actual_date}"
        mkdir -p "${PERF_TARGET_DIR}"

        dst_file="${PERF_TARGET_DIR}/${subdir_name_clean}__${CURRENT_DATE}.txt"
        cp "${src_file}" "${dst_file}"

        # 在文件末尾追加原始修改时间描述
        mtime_human=$(date -d "@${mtime_epoch}" '+%Y-%m-%d %H:%M:%S' 2>/dev/null || date -r "${mtime_epoch}" '+%Y-%m-%d %H:%M:%S' 2>/dev/null)
        {
            echo ""
            echo "# [collect_metrics] 文件原始修改时间: ${mtime_human}"
            echo "# [collect_metrics] 源目录日期: ${CURRENT_DATE}"
            echo "# [collect_metrics] CI运行目录: ${subdir_name}"
        } >> "${dst_file}"

        echo "[OK] ${subdir_name_clean} (源目录日期: ${CURRENT_DATE}, 实际修改日期: ${actual_date})"
        count=$((count + 1))
    done < <(find "${SRC_BASE}" -type f -name 'bench_serving_metrics.txt' -path '*/perf/*')

    echo ""
    echo "完成: 共收集 ${count} 个性能测试文件（按实际修改时间归类）"
    TOTAL_PERF_COUNT=$((TOTAL_PERF_COUNT + count))

    # ============================================================
    # 收集精度测试结果 (eval_log.log)
    # 新 CI 结构: SRC_BASE/{branch}-{run_id}/{workflow_type}/{test_type}/{tc_name}-{timestamp}/logs/eval_log.log
    # 所有 perf 和 accuracy 类型的 eval 日志都在 SRC_BASE 下统一搜索
    # 存储到: SCRIPT_DIR/实际日期/eval/ 下，按"用例名__时间戳__源日期.log"命名
    # ============================================================

    eval_count=0
    while IFS= read -r eval_src; do
        [ -f "${eval_src}" ] || continue

        # 新结构路径: .../output/{branch}-{run_id}/{workflow_type}/{test_type}/{tc_name}-{timestamp}/logs/eval_log.log
        logs_dir=$(dirname "${eval_src}")
        ts_dir=$(dirname "${logs_dir}")           # .../{tc_name}-{timestamp}
        ts_name=$(basename "${ts_dir}")           # {tc_name}-{timestamp}
        # 剥离 CI 时间戳后缀，保留干净的用例名
        ts_name_clean=$(echo "${ts_name}" | sed 's/-[0-9]\{6\}$//')
        test_type_dir=$(dirname "${ts_dir}")      # .../{test_type}
        test_type_name=$(basename "${test_type_dir}")  # perf / accuracy

        # 获取文件实际修改时间（秒级时间戳），兼容 Linux/macOS
        mtime_epoch=$(stat -c '%Y' "${eval_src}" 2>/dev/null || stat -f '%m' "${eval_src}" 2>/dev/null)
        if [ -z "${mtime_epoch}" ]; then
            echo "[WARN-EVAL] ${test_type_name}__${ts_name}: 无法获取文件修改时间，跳过"
            continue
        fi

        actual_date=$(date -d "@${mtime_epoch}" +%Y%m%d 2>/dev/null || date -r "${mtime_epoch}" +%Y%m%d 2>/dev/null)
        if [ -z "${actual_date}" ]; then
            echo "[WARN-EVAL] ${test_type_name}__${ts_name}: 无法转换修改时间，跳过"
            continue
        fi

        EVAL_TARGET_DIR="${SCRIPT_DIR}/${actual_date}/eval"
        mkdir -p "${EVAL_TARGET_DIR}"

        # 命名: {test_type}__{tc_name_clean}__{源目录日期}.log
        eval_dst="${EVAL_TARGET_DIR}/${test_type_name}__${ts_name_clean}__${CURRENT_DATE}.log"
        # 如果已存在同名文件（来自不同 workflow_type 等），追加序号后缀区分
        if [ -f "${eval_dst}" ]; then
            suffix=1
            while [ -f "${EVAL_TARGET_DIR}/${test_type_name}__${ts_name_clean}__${CURRENT_DATE}-${suffix}.log" ]; do
                suffix=$((suffix + 1))
            done
            eval_dst="${EVAL_TARGET_DIR}/${test_type_name}__${ts_name_clean}__${CURRENT_DATE}-${suffix}.log"
        fi
        cp "${eval_src}" "${eval_dst}"

        # 在文件末尾追加原始修改时间描述
        mtime_human=$(date -d "@${mtime_epoch}" '+%Y-%m-%d %H:%M:%S' 2>/dev/null || date -r "${mtime_epoch}" '+%Y-%m-%d %H:%M:%S' 2>/dev/null)
        {
            echo ""
            echo "# [collect_metrics] 文件原始修改时间: ${mtime_human}"
        } >> "${eval_dst}"

        echo "[EVAL] ${test_type_name}__${ts_name_clean} (源目录日期: ${CURRENT_DATE}, 实际修改日期: ${actual_date})"
        eval_count=$((eval_count + 1))
    done < <(find "${SRC_BASE}" -type f -name 'eval_log.log' -path '*/logs/eval_log.log')

    if [ ${eval_count} -gt 0 ]; then
        echo ""
        echo "完成: 共收集 ${eval_count} 个精度测试文件（按实际修改时间归类）"
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

# 拷贝脚本所在路径下所有目录及文件到目标路径（排除 .git 和自身临时目录）
echo "拷贝文件到仓库..."
rsync -a --delete \
    --exclude='.git' \
    --exclude='.all_test_in_repo' \
    --exclude='collect_metrics.sh' \
    "${SCRIPT_DIR}/" "${GIT_LOCAL_DIR}/${GIT_TARGET_PATH}/"

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
