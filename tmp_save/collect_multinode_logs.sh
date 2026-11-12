#!/usr/bin/env bash
# 收集指定日期的多机（test_npu_*）任务日志，打包后上传到 Gitee 个人数据仓的 tmp_save 目录。
#
# 日志目录约定（与数据仓 collect_metrics.sh 一致）：
#   LOG_BASE/{branch}-{date}-{run_id}-{attempt}/{workflow}/test_npu_*/
#   默认 LOG_BASE=/data/ascend-ci-share-pkking-sglang/tests/logs/log
#
# 用法：
#   export GITEE_TOKEN=xxxxxxxx
#   ./collect_multinode_logs.sh --date 20261109
#   ./collect_multinode_logs.sh --date 20261109 --branch main --case kimi_k2_6 --exclude-plog
#   ./collect_multinode_logs.sh --date 20261109 --dry-run
#
# 注意：Gitee 对单文件大小有限制，默认超过 MAX_ARCHIVE_MB(100MB) 的包会被跳过，
#       可用 --case 缩小范围、--exclude-plog 排除 plog，或 --max-mb 调整阈值。

set -euo pipefail
export GIT_TERMINAL_PROMPT=0

LOG_BASE="${LOG_BASE:-/data/ascend-ci-share-pkking-sglang/tests/logs/log}"
GIT_REPO="${GIT_REPO:-https://gitee.com/pllimax_admin/all_test_in.git}"
GIT_BRANCH="${GIT_BRANCH:-main}"
GIT_TARGET_PATH="${GIT_TARGET_PATH:-tmp_save}"
GIT_USER_NAME="${GIT_USER_NAME:-pllimax}"
GIT_USER_EMAIL="${GIT_USER_EMAIL:-pllimax2556769@163.com}"
MAX_ARCHIVE_MB="${MAX_ARCHIVE_MB:-100}"
UPLOAD_RETRY="${UPLOAD_RETRY:-3}"
UPLOAD_RETRY_DELAY="${UPLOAD_RETRY_DELAY:-10}"

DATES_INPUT=""
BRANCH_FILTER=""
WF_FILTER=""
CASE_FILTER=""
EXCLUDE_PLOG=0
DRY_RUN=0

usage() {
    cat <<'EOF'
用法: collect_multinode_logs.sh --date YYYYMMDD[,YYYYMMDD...] [选项]

选项:
  -d, --date DATE     要收集的日期（必填），支持 20261109 或 2026-11-09，多个用逗号分隔
  -b, --branch PREFIX 只收集 CI 目录名以 PREFIX- 开头的 run（如 main）
  -w, --wf NAME       workflow 前缀过滤（忽略 --镜像标签 后缀，如 Nightly_Test_NPU）
  -c, --case KEY      test_npu_* 用例名包含 KEY 才收集（如 kimi_k2_6）
      --exclude-plog  打包时排除 plog 目录（体积大，通常非必需）
      --max-mb N      单个压缩包大小上限，单位 MB（默认 100，超过则跳过并提示）
      --dry-run       只收集打包并列出结果，不推送
  -h, --help          显示帮助

环境变量:
  GITEE_TOKEN         Gitee 私人令牌（推送 https 仓库时必填，自动按 oauth2:TOKEN 拼接）
  LOG_BASE            多机日志根目录，默认 /data/ascend-ci-share-pkking-sglang/tests/logs/log
  GIT_REPO            数据仓地址，默认 https://gitee.com/pllimax_admin/all_test_in.git
  GIT_BRANCH          推送分支，默认 main
  GIT_TARGET_PATH     仓库内目标目录，默认 tmp_save
  MAX_ARCHIVE_MB      单包大小上限（MB），默认 100
  UPLOAD_RETRY        推送失败重试次数，默认 3
  UPLOAD_RETRY_DELAY  重试间隔秒数，默认 10

示例:
  GITEE_TOKEN=xxxx ./collect_multinode_logs.sh -d 20261109
  GITEE_TOKEN=xxxx ./collect_multinode_logs.sh -d 20261109 -b main -c kimi_k2_6 --exclude-plog
EOF
}

die() {
    echo "错误: $*" >&2
    exit 1
}

log() {
    echo "[$(date '+%H:%M:%S')] $*"
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        -d|--date)
            [[ $# -ge 2 ]] || die "$1 缺少参数"
            DATES_INPUT="$2"
            shift 2
            ;;
        -b|--branch)
            [[ $# -ge 2 ]] || die "$1 缺少参数"
            BRANCH_FILTER="$2"
            shift 2
            ;;
        -w|--wf)
            [[ $# -ge 2 ]] || die "$1 缺少参数"
            WF_FILTER="$2"
            shift 2
            ;;
        -c|--case)
            [[ $# -ge 2 ]] || die "$1 缺少参数"
            CASE_FILTER="$2"
            shift 2
            ;;
        --exclude-plog)
            EXCLUDE_PLOG=1
            shift
            ;;
        --max-mb)
            [[ $# -ge 2 ]] || die "$1 缺少参数"
            MAX_ARCHIVE_MB="$2"
            shift 2
            ;;
        --dry-run)
            DRY_RUN=1
            shift
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        *)
            echo "未知参数: $1" >&2
            usage >&2
            exit 1
            ;;
    esac
done

[[ -n "${DATES_INPUT}" ]] || { usage >&2; die "缺少 --date"; }
[[ -d "${LOG_BASE}" ]] || die "日志根目录不存在: ${LOG_BASE}"
[[ "${MAX_ARCHIVE_MB}" =~ ^[0-9]+$ ]] || die "--max-mb 需为整数: ${MAX_ARCHIVE_MB}"

IFS=', ' read -r -a DATES <<< "${DATES_INPUT}"
for i in "${!DATES[@]}"; do
    d="${DATES[$i]//-/}"
    [[ "${d}" =~ ^[0-9]{8}$ ]] || die "日期格式错误: ${DATES[$i]}（应为 YYYYMMDD）"
    DATES[$i]="${d}"
done
DATES_STR=$(IFS=,; echo "${DATES[*]}")

TMP_DIR="$(mktemp -d)"
trap 'rm -rf "${TMP_DIR}"' EXIT

log "日志根目录: ${LOG_BASE}"
log "收集日期:   ${DATES_STR}"
log "过滤条件:   branch=${BRANCH_FILTER:-全部}, workflow=${WF_FILTER:-全部}, case=${CASE_FILTER:-全部}, exclude_plog=${EXCLUDE_PLOG}"

ARCHIVES=()
TOTAL_CASES=0
SKIPPED=0

for DATE in "${DATES[@]}"; do
    log "扫描日期 ${DATE} 的 run 目录 ..."
    mapfile -t RUN_DIRS < <(find "${LOG_BASE}" -mindepth 1 -maxdepth 1 -type d -name "*-${DATE}-*-*" | sort)
    if (( ${#RUN_DIRS[@]} == 0 )); then
        log "未找到日期 ${DATE} 的 run 目录"
        continue
    fi

    for run_dir in "${RUN_DIRS[@]}"; do
        run_name=$(basename "${run_dir}")
        if [[ -n "${BRANCH_FILTER}" && "${run_name}" != "${BRANCH_FILTER}-"* ]]; then
            continue
        fi

        list_file="${TMP_DIR}/${run_name}.list"
        : > "${list_file}"
        case_count=0

        for wf_dir in "${run_dir}"/*/; do
            [[ -d "${wf_dir}" ]] || continue
            wf_name=$(basename "${wf_dir}")
            if [[ -n "${WF_FILTER}" && "${wf_name%%--*}" != "${WF_FILTER}"* ]]; then
                continue
            fi
            for case_dir in "${wf_dir}"test_npu_*/; do
                [[ -d "${case_dir}" ]] || continue
                case_name=$(basename "${case_dir}")
                if [[ -n "${CASE_FILTER}" && "${case_name}" != *"${CASE_FILTER}"* ]]; then
                    continue
                fi
                printf '%s/%s/%s\n' "${run_name}" "${wf_name}" "${case_name}" >> "${list_file}"
                case_count=$((case_count + 1))
            done
        done

        if (( case_count == 0 )); then
            log "跳过 ${run_name}: 没有匹配的多机用例日志"
            continue
        fi

        out="${TMP_DIR}/multinode_logs_${run_name}.tar.gz"
        # 注意: GNU tar 的 --exclude 是位置参数，必须在 -T 之前，否则不生效
        tar_opts=(-czf "${out}" -C "${LOG_BASE}")
        if (( EXCLUDE_PLOG )); then
            tar_opts+=(--exclude='*/plog' --exclude='*/plog/*')
        fi
        tar_opts+=(-T "${list_file}")

        log "打包 ${run_name}（${case_count} 个用例目录）..."
        rc=0
        tar "${tar_opts[@]}" || rc=$?
        if (( rc >= 2 )); then
            die "打包失败(rc=${rc}): ${run_name}"
        elif (( rc == 1 )); then
            echo "  警告: 打包时有文件变化，压缩包可能不完整（日志仍在写入？）"
        fi

        size_bytes=$(wc -c < "${out}")
        size_mb=$(( (size_bytes + 1024 * 1024 - 1) / (1024 * 1024) ))
        if (( size_mb > MAX_ARCHIVE_MB )); then
            echo "  跳过 ${run_name}: 压缩包 ${size_mb}MB 超过上限 ${MAX_ARCHIVE_MB}MB"
            echo "        可用 --case 缩小用例范围、--exclude-plog 排除 plog，或 --max-mb 调高阈值"
            echo "        各用例日志体积:"
            while IFS= read -r rel; do
                printf '          %8s  %s\n' "$(du -sh "${LOG_BASE}/${rel}" | cut -f1)" "${rel##*/}"
            done < "${list_file}"
            rm -f "${out}"
            SKIPPED=$((SKIPPED + 1))
            continue
        fi

        ARCHIVES+=("${out}")
        TOTAL_CASES=$((TOTAL_CASES + case_count))
        echo "  -> $(basename "${out}") (${size_mb}MB, ${case_count} 个用例)"
    done
done

echo
if (( ${#ARCHIVES[@]} == 0 )); then
    log "没有可上传的日志包（超限跳过 ${SKIPPED} 个）"
    exit 0
fi

log "待上传 ${#ARCHIVES[@]} 个压缩包，共 ${TOTAL_CASES} 个用例目录:"
ls -lh "${ARCHIVES[@]}"

if (( DRY_RUN )); then
    log "--dry-run: 跳过上传"
    exit 0
fi

if [[ "${GIT_REPO}" == https://* ]]; then
    [[ -n "${GITEE_TOKEN:-}" ]] || die "推送 https 仓库需要设置 GITEE_TOKEN"
    CLONE_URL="https://oauth2:${GITEE_TOKEN}@${GIT_REPO#https://}"
else
    CLONE_URL="${GIT_REPO}"
fi

GIT_LOG="${TMP_DIR}/git.log"
WORK_REPO="${TMP_DIR}/all_test_in_main"

mask() {
    if [[ -n "${GITEE_TOKEN:-}" ]]; then
        sed "s|${GITEE_TOKEN}|***|g"
    else
        cat
    fi
}

upload_once() {
    rm -rf "${WORK_REPO}"
    if ! git clone --depth=1 --branch "${GIT_BRANCH}" "${CLONE_URL}" "${WORK_REPO}" > "${GIT_LOG}" 2>&1; then
        echo "git clone 失败:" >&2
        mask < "${GIT_LOG}" >&2
        return 1
    fi

    rc=0
    (
        set -e
        cd "${WORK_REPO}"
        mkdir -p "${GIT_TARGET_PATH}"
        cp "${ARCHIVES[@]}" "${GIT_TARGET_PATH}/"
        git add "${GIT_TARGET_PATH}"
        if git diff --cached --quiet; then
            echo "__NOTHING_TO_COMMIT__"
            exit 0
        fi
        git -c user.name="${GIT_USER_NAME}" -c user.email="${GIT_USER_EMAIL}" \
            commit -m "upload multinode logs: ${DATES_STR}"
        git push origin "HEAD:${GIT_BRANCH}"
    ) > "${GIT_LOG}" 2>&1 || rc=$?

    if (( rc != 0 )); then
        echo "git 提交/推送失败:" >&2
        mask < "${GIT_LOG}" >&2
        return 1
    fi
    if grep -q "__NOTHING_TO_COMMIT__" "${GIT_LOG}"; then
        log "远端 ${GIT_TARGET_PATH}/ 已存在同名压缩包，无需提交"
    fi
    return 0
}

OK=0
for ((i = 1; i <= UPLOAD_RETRY; i++)); do
    log "上传到 ${GIT_REPO} (${GIT_BRANCH}:${GIT_TARGET_PATH})，第 ${i}/${UPLOAD_RETRY} 次 ..."
    if upload_once; then
        OK=1
        break
    fi
    if (( i < UPLOAD_RETRY )); then
        log "${UPLOAD_RETRY_DELAY}s 后重试 ..."
        sleep "${UPLOAD_RETRY_DELAY}"
    fi
done
(( OK )) || die "上传失败，请检查网络、GITEE_TOKEN 或仓库容量限制"

echo
log "上传完成:"
for a in "${ARCHIVES[@]}"; do
    echo "  ${GIT_TARGET_PATH}/$(basename "${a}")"
done
echo "仓库地址: ${GIT_REPO%.git}/tree/${GIT_BRANCH}/${GIT_TARGET_PATH}"
