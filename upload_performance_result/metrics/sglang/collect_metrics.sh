#!/bin/bash

# 用法:
#   自动收集: ./collect_metrics.sh                    (收集今天及前3天数据)
#   指定日期: ./collect_metrics.sh 20260716
#   自定义配置: SRC_BASE=/custom/path GIT_REPO=git@github.com:user/repo.git ./collect_metrics.sh 20260716
#   使用配置文件: ./collect_metrics.sh 20260716 --config /path/to/config.conf
#   命令行覆盖: ./collect_metrics.sh --src-base /custom/path --git-repo git@github.com:user/repo.git 20260716
# 从指定目录下各子目录中收集 bench_serving_metrics.txt 文件

set -e

# ============================================================
# 配置项：优先使用环境变量，提供默认值
# ============================================================
SRC_BASE="${SRC_BASE:-/data/ascend-ci-share-pkking-sglang/tests/output/perf}"
GIT_REPO="${GIT_REPO:-git@github.com-pllimax:pllimax/all_test_in.git}"
GIT_TARGET_PATH="${GIT_TARGET_PATH:-upload_performance_result/metrics/sglang}"
GIT_LOCAL_DIR="${GIT_LOCAL_DIR:-}"

# ============================================================
# 参数解析
# ============================================================
DATE=""

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
            echo "用法: $0 [选项] [日期]"
            echo ""
            echo "参数:"
            echo "  日期                  收集数据的日期，格式如 20260716"
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
            echo "  $0 20260716"
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
            if [ -z "$DATE" ]; then
                DATE="$1"
            else
                echo "错误: 未知参数 $1"
                exit 1
            fi
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
if [ -z "$DATE" ]; then
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
    DATES=("$DATE")
fi

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# 设置 Git 本地目录默认值（依赖 SCRIPT_DIR）
if [ -z "$GIT_LOCAL_DIR" ]; then
    GIT_LOCAL_DIR="${SCRIPT_DIR}/.all_test_in_repo"
fi

# 精度数据来源基础路径（常量，不随日期变化）
EVAL2_SRC_BASE="${EVAL2_SRC_BASE:-/data/ascend-ci-share-pkking-sglang/tests/output}"
ACC_SRC_BASE="${ACC_SRC_BASE:-/data/ascend-ci-share-pkking-sglang/tests/output/accuracy}"

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
    echo "日期:           ${DATE}"
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

    SRC_FULL_PATH="${SRC_BASE}/${CURRENT_DATE}"
    TARGET_DIR="${SCRIPT_DIR}/${CURRENT_DATE}"
    mkdir -p "${TARGET_DIR}"

    if [ ! -d "${SRC_FULL_PATH}" ]; then
        if [ "$AUTO_MODE" = true ]; then
            echo "跳过: 源目录不存在 - ${SRC_FULL_PATH}"
            continue
        else
            echo "错误: 源目录不存在: ${SRC_FULL_PATH}"
            echo ""
            echo "可能的原因:"
            echo "  1. 日期参数错误"
            echo "  2. SRC_BASE 配置不正确（当前值: ${SRC_BASE}）"
            echo "  3. 数据尚未生成"
            echo ""
            echo "解决方法:"
            echo "  - 检查日期参数是否正确"
            echo "  - 通过环境变量设置正确的路径: SRC_BASE=/correct/path $0 ${CURRENT_DATE}"
            echo "  - 或通过命令行参数: $0 --src-base /correct/path ${CURRENT_DATE}"
            exit 1
        fi
    fi

    echo "源目录: ${SRC_FULL_PATH}"
    echo "目标目录: ${TARGET_DIR}"
    echo ""

    count=0
    for subdir in "${SRC_FULL_PATH}"/*/; do
        [ -d "${subdir}" ] || continue

        subdir_name=$(basename "${subdir}")
        src_file="${subdir}bench_serving_metrics.txt"

        if [ -f "${src_file}" ]; then
            cp "${src_file}" "${TARGET_DIR}/${subdir_name}.txt"
            echo "[OK] ${subdir_name}"
            count=$((count + 1))
        else
            echo "[SKIP] ${subdir_name} (无 bench_serving_metrics.txt)"
        fi
    done

    echo ""
    echo "完成: 共收集 ${count} 个性能测试文件到 ${TARGET_DIR}"
    TOTAL_PERF_COUNT=$((TOTAL_PERF_COUNT + count))

    # ============================================================
    # 收集所有来源的精度测试结果 (eval_log.log)
    # 来源1: SRC_BASE/DATE/.../logs/eval_log.log (perf测试伴随的精度测试)
    # 来源2: /data/.../tests/output/DATE/.../logs/eval_log.log (补充精度测试)
    # 来源3: /data/.../tests/output/accuracy/DATE/.../logs/eval_log.log (仅精度测试)
    # 统一存储到: TARGET_DIR/eval/ 下，按"用例名__时间戳.log"命名
    # 同名文件以来源标签后缀区分
    # ============================================================
    EVAL_TARGET_DIR="${TARGET_DIR}/eval"
    mkdir -p "${EVAL_TARGET_DIR}"

    eval_sources_config=(
        "${SRC_BASE}:perf"
        "${EVAL2_SRC_BASE}:output"
        "${ACC_SRC_BASE}:accuracy"
    )

    eval_count=0
    for src_entry in "${eval_sources_config[@]}"; do
        src_base="${src_entry%%:*}"
        src_label="${src_entry##*:}"
        src_path="${src_base}/${CURRENT_DATE}"

        [ -d "${src_path}" ] || continue

        for subdir in "${src_path}"/*/; do
            [ -d "${subdir}" ] || continue
            subdir_name=$(basename "${subdir}")

            for ts_dir in "${subdir}"*/; do
                [ -d "${ts_dir}" ] || continue
                ts_name=$(basename "${ts_dir}")
                eval_src="${ts_dir}logs/eval_log.log"

                if [ -f "${eval_src}" ]; then
                    eval_dst="${EVAL_TARGET_DIR}/${subdir_name}__${ts_name}.log"
                    # 如果已存在同名文件（来自其他来源），添加来源标签后缀区分
                    if [ -f "${eval_dst}" ]; then
                        eval_dst="${EVAL_TARGET_DIR}/${subdir_name}__${ts_name}-${src_label}.log"
                    fi
                    cp "${eval_src}" "${eval_dst}"
                    echo "[EVAL-${src_label}] ${subdir_name}__${ts_name}"
                    eval_count=$((eval_count + 1))
                fi
            done
        done
    done

    if [ ${eval_count} -gt 0 ]; then
        echo ""
        echo "完成: 共收集 ${eval_count} 个精度测试文件到 ${EVAL_TARGET_DIR}"
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
    git fetch origin --depth=1
    git reset --hard origin/main 2>/dev/null || git reset --hard origin/master 2>/dev/null
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
    if [ "$AUTO_MODE" = true ]; then
        git commit -m "update metrics data - ${DATES[0]}~${DATES[-1]}"
    else
        git commit -m "update metrics data - ${DATE}"
    fi
    git push origin HEAD
    echo "上传成功!"
fi

echo "========== 上传完成 =========="
