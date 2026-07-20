#!/bin/bash

# 用法: ./collect_metrics.sh 20260716
# 从指定目录下各子目录中收集 bench_serving_metrics.txt 文件

set -e

DATE="${1:?请提供日期参数，例如: ./collect_metrics.sh 20260716}"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SRC_BASE="/data/ascend-ci-share-pkking-sglang/tests/output/perf/${DATE}"

# 在脚本所在路径创建日期文件夹
TARGET_DIR="${SCRIPT_DIR}/${DATE}"
mkdir -p "${TARGET_DIR}"

if [ ! -d "${SRC_BASE}" ]; then
    echo "错误: 源目录不存在: ${SRC_BASE}"
    exit 1
fi

echo "源目录: ${SRC_BASE}"
echo "目标目录: ${TARGET_DIR}"
echo ""

count=0
for subdir in "${SRC_BASE}"/*/; do
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
echo "完成: 共收集 ${count} 个文件到 ${TARGET_DIR}"

# ============================================================
# 上传到 Git 仓库
# ============================================================
GIT_REPO="git@github.com-pllimax:pllimax/all_test_in.git"
GIT_TARGET_PATH="upload_performance_result/metrics/sglang"
GIT_LOCAL_DIR="${SCRIPT_DIR}/.all_test_in_repo"

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
