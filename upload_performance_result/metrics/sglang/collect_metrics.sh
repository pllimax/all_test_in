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
