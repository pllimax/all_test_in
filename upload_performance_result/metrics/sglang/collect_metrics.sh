#!/bin/bash

# 用法:
#   基本用法: ./collect_metrics.sh 20260716
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
            echo "用法: $0 [选项] <日期>"
            echo ""
            echo "参数:"
            echo "  日期                  收集数据的日期，格式如 20260716"
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

# 验证必需参数
if [ -z "$DATE" ]; then
    echo "错误: 请提供日期参数"
    echo "用法: $0 <日期>"
    echo "示例: $0 20260716"
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# 设置 Git 本地目录默认值（依赖 SCRIPT_DIR）
if [ -z "$GIT_LOCAL_DIR" ]; then
    GIT_LOCAL_DIR="${SCRIPT_DIR}/.all_test_in_repo"
fi

SRC_FULL_PATH="${SRC_BASE}/${DATE}"

# 在脚本所在路径创建日期文件夹
TARGET_DIR="${SCRIPT_DIR}/${DATE}"
mkdir -p "${TARGET_DIR}"

# ============================================================
# 配置验证
# ============================================================
echo "========== 配置信息 =========="
echo "源目录基础路径: ${SRC_BASE}"
echo "完整源路径:     ${SRC_FULL_PATH}"
echo "Git仓库:        ${GIT_REPO}"
echo "Git目标路径:    ${GIT_TARGET_PATH}"
echo "=============================="
echo ""

if [ ! -d "${SRC_FULL_PATH}" ]; then
    echo "错误: 源目录不存在: ${SRC_FULL_PATH}"
    echo ""
    echo "可能的原因:"
    echo "  1. 日期参数错误"
    echo "  2. SRC_BASE 配置不正确（当前值: ${SRC_BASE}）"
    echo "  3. 数据尚未生成"
    echo ""
    echo "解决方法:"
    echo "  - 检查日期参数是否正确"
    echo "  - 通过环境变量设置正确的路径: SRC_BASE=/correct/path $0 ${DATE}"
    echo "  - 或通过命令行参数: $0 --src-base /correct/path ${DATE}"
    exit 1
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

# ============================================================
# 收集精度测试结果 (eval_log.log)
# 目录结构: SRC_BASE/DATE/test_case_name/时间戳/logs/eval_log.log
# 如果有多个时间戳，全部拷贝并以时间戳区分命名
# ============================================================
EVAL_TARGET_DIR="${TARGET_DIR}/eval"
mkdir -p "${EVAL_TARGET_DIR}"

eval_count=0
for subdir in "${SRC_FULL_PATH}"/*/; do
    [ -d "${subdir}" ] || continue

    subdir_name=$(basename "${subdir}")

    # 遍历用例目录下的所有时间戳子目录
    for ts_dir in "${subdir}"*/; do
        [ -d "${ts_dir}" ] || continue

        ts_name=$(basename "${ts_dir}")
        eval_src="${ts_dir}logs/eval_log.log"

        if [ -f "${eval_src}" ]; then
            # 目标文件名: 用例名__时间戳.log (双下划线区分用例名和时间戳)
            eval_dst="${EVAL_TARGET_DIR}/${subdir_name}__${ts_name}.log"
            cp "${eval_src}" "${eval_dst}"
            echo "[EVAL] ${subdir_name}__${ts_name}"
            eval_count=$((eval_count + 1))
        fi
    done
done

echo ""
echo "完成: 共收集 ${eval_count} 个精度测试文件到 ${EVAL_TARGET_DIR}"

# ============================================================
# 收集仅精度测试结果 (accuracy-only)
# 目录结构: /data/.../tests/output/accuracy/DATE/test_case_name/时间戳/logs/eval_log.log
# 这些用例没有性能测试数据，仅有精度评估结果
# ============================================================
ACC_SRC_BASE="${ACC_SRC_BASE:-/data/ascend-ci-share-pkking-sglang/tests/output/accuracy}"
ACC_SRC_FULL_PATH="${ACC_SRC_BASE}/${DATE}"
ACC_TARGET_DIR="${TARGET_DIR}/accuracy"
mkdir -p "${ACC_TARGET_DIR}"

acc_count=0
if [ -d "${ACC_SRC_FULL_PATH}" ]; then
    for subdir in "${ACC_SRC_FULL_PATH}"/*/; do
        [ -d "${subdir}" ] || continue

        subdir_name=$(basename "${subdir}")

        # 遍历用例目录下的所有时间戳子目录
        for ts_dir in "${subdir}"*/; do
            [ -d "${ts_dir}" ] || continue

            ts_name=$(basename "${ts_dir}")
            acc_src="${ts_dir}logs/eval_log.log"

            if [ -f "${acc_src}" ]; then
                # 目标文件名: 用例名__时间戳.log
                acc_dst="${ACC_TARGET_DIR}/${subdir_name}__${ts_name}.log"
                cp "${acc_src}" "${acc_dst}"
                echo "[ACC] ${subdir_name}__${ts_name}"
                acc_count=$((acc_count + 1))
            fi
        done
    done
    echo ""
    echo "完成: 共收集 ${acc_count} 个仅精度测试文件到 ${ACC_TARGET_DIR}"
else
    echo ""
    echo "[SKIP] 精度测试源目录不存在: ${ACC_SRC_FULL_PATH}"
fi

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
    git commit -m "update metrics data - ${DATE}"
    git push origin HEAD
    echo "上传成功!"
fi

echo "========== 上传完成 =========="
