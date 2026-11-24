#!/usr/bin/env bash
# 清理 Ascend CI 共享盘上的历史产物。
#
# 目录布局（依据 python/sglang/test/ascend/e2e/ 与 .github/workflows/ 中的生成逻辑）：
#   ${BASE}/logs/log/${run_label}/${workflow_name}/${test_type}/${tc_name}/${HOSTNAME}   # 执行日志
#   ${BASE}/logs/log/${YYYYMMDD}/${tc_name}/${HOSTNAME}                                  # PR 旧布局
#   ${BASE}/logs/plog/${run_label}/${workflow_name}/${tc_name}/${HOSTNAME}               # 框架 plog
#   ${BASE}/output/${run_label}/${workflow_name}/${test_type}/${tc_name}                 # 执行结果
#   ${BASE}/sglang-${GITHUB_RUN_ID}                                                      # 临时分支代码
# 其中 run_label = ${branch_label}-${create_time}-${run_id}-${run_attempt}。
#
# 本脚本只按第一层目录处理，且只删除名字符合上述格式的目录，其他目录仅提示、不删除。
# 默认先统计并等待确认，确认后才删除；单次最多删除 --limit 个目录（默认 100）。
#
# 用法示例：
#   ./cleanup_ci_storage.sh                          # 统计 + 交互确认后删除
#   ./cleanup_ci_storage.sh --dry-run                # 只统计，不删除
#   ./cleanup_ci_storage.sh -y --limit 100           # 跳过确认，最多删 100 个
#   ./cleanup_ci_storage.sh --base-path /data/tests --logs-days 30

set -euo pipefail

# 统一按字节处理，避免中文键/海量目录下 locale 影响正则与排序（UTF-8 输出不受影响）
export LC_ALL=C

BASE_PATH="/mnt/sfs-local/ascend-ci-share/tests"
LOGS_DIR=""
PLOG_DIR=""
OUTPUT_DIR=""
LOGS_DAYS=60
PLOG_DAYS=60
OUTPUT_DAYS=60
TEMP_DAYS=7
LIMIT=100
ASSUME_YES=0
DRY_RUN=0

# 第一层目录的合法命名：nightly 的 run_label 或 PR 旧布局的日期目录
readonly RUN_DIR_RE='-[0-9]{8}-[0-9]{4}-[0-9]+-[0-9]+$'
readonly DATE_DIR_RE='^[0-9]{8}$'
# 临时分支代码目录：sglang-${run_id}
readonly TEMP_DIR_RE='^sglang-[0-9]+$'

usage() {
    # 打印文件顶部的注释块（跳过 shebang，遇到第一行非注释即停止）
    awk 'NR > 1 { if ($0 !~ /^#/) exit; sub(/^# ?/, ""); print }' "$0"
    cat <<'EOF'

可配置参数:
  -b, --base-path PATH   CI 共享盘基本路径 (默认 /mnt/sfs-local/ascend-ci-share/tests)
      --logs-dir PATH    执行日志目录 (默认 ${BASE}/logs/log)
      --plog-dir PATH    框架日志目录 (默认 ${BASE}/logs/plog)
      --output-dir PATH  执行结果目录 (默认 ${BASE}/output)
      --logs-days N      执行日志保留天数 (默认 60)
      --plog-days N      框架日志保留天数 (默认 60)
      --output-days N    执行结果保留天数 (默认 60)
      --temp-days N      临时分支代码保留天数 (默认 7)
      --limit N          单次最多删除的目录数 (默认 100)
  -n, --dry-run          只统计，不删除
  -y, --yes              跳过交互确认直接删除
  -h, --help             显示帮助
EOF
}

die() { echo "ERROR: $*" >&2; exit 1; }

while [[ $# -gt 0 ]]; do
    case "$1" in
        -b|--base-path) BASE_PATH="${2:?}"; shift 2 ;;
        --logs-dir) LOGS_DIR="${2:?}"; shift 2 ;;
        --plog-dir) PLOG_DIR="${2:?}"; shift 2 ;;
        --output-dir) OUTPUT_DIR="${2:?}"; shift 2 ;;
        --logs-days) LOGS_DAYS="${2:?}"; shift 2 ;;
        --plog-days) PLOG_DAYS="${2:?}"; shift 2 ;;
        --output-days) OUTPUT_DAYS="${2:?}"; shift 2 ;;
        --temp-days) TEMP_DAYS="${2:?}"; shift 2 ;;
        --limit) LIMIT="${2:?}"; shift 2 ;;
        -n|--dry-run) DRY_RUN=1; shift ;;
        -y|--yes) ASSUME_YES=1; shift ;;
        -h|--help) usage; exit 0 ;;
        *) die "未知参数: $1 (使用 --help 查看用法)" ;;
    esac
done

[[ "$BASE_PATH" == /* ]] || die "基本路径必须是绝对路径: ${BASE_PATH}"
[[ "$BASE_PATH" != "/" ]] || die "基本路径不能是根目录 /"
[[ -d "$BASE_PATH" ]] || die "基本路径不存在: ${BASE_PATH}"
for v in LOGS_DAYS PLOG_DAYS OUTPUT_DAYS TEMP_DAYS LIMIT; do
    [[ "${!v}" =~ ^[0-9]+$ ]] || die "$v 必须是整数: ${!v}"
done
(( LIMIT > 0 )) || die "--limit 必须大于 0"

BASE_PATH="$(cd "$BASE_PATH" && pwd -P)"
[[ -n "$LOGS_DIR" ]] || LOGS_DIR="${BASE_PATH}/logs/log"
[[ -n "$PLOG_DIR" ]] || PLOG_DIR="${BASE_PATH}/logs/plog"
[[ -n "$OUTPUT_DIR" ]] || OUTPUT_DIR="${BASE_PATH}/output"

for d in "$LOGS_DIR" "$PLOG_DIR" "$OUTPUT_DIR"; do
    [[ "$d" == /* ]] || die "目录必须是绝对路径: ${d}"
    [[ "$d" != "/" ]] || die "目录不能是根目录 /: ${d}"
done

command -v find >/dev/null || die "缺少 find 命令"
command -v du >/dev/null || die "缺少 du 命令"

# 采集结果：每行 "mtime_epoch<TAB>分类<TAB>路径"
TMP_LIST="$(mktemp)"
trap 'rm -f "$TMP_LIST"' EXIT

declare -A CNT=() SIZE_KB=() SKIPPED=()
declare -a ORDER=()

# collect <分类名> <目录> <保留天数> <允许的名字正则> [只统计此前缀的跳过项]
collect() {
    local name="$1" dir="$2" days="$3" re="$4" skip_prefix="${5:-}"
    local total=0 skipped=0 t p base

    CNT["$name"]=0
    SKIPPED["$name"]=0
    ORDER+=("$name")

    if [[ ! -d "$dir" ]]; then
        echo "WARN: 目录不存在，跳过: ${dir}" >&2
        return
    fi

    while IFS=$'\t' read -r t p; do
        [[ -n "$p" ]] || continue
        base="${p##*/}"
        if [[ "$base" =~ $re ]]; then
            printf '%s\t%s\t%s\n' "$t" "$name" "$p" >> "$TMP_LIST"
            total=$((total + 1))
        elif [[ -z "$skip_prefix" || "$base" == "$skip_prefix"* ]]; then
            skipped=$((skipped + 1))
        fi
    done < <(find "$dir" -mindepth 1 -maxdepth 1 -type d -mtime +"$days" -printf '%T@\t%p\n' 2>/dev/null | sort -n)

    CNT["$name"]=$total
    SKIPPED["$name"]=$skipped
}

echo "CI 共享盘清理检查"
echo "  基本路径      : ${BASE_PATH}"
echo "  执行日志      : ${LOGS_DIR}   (> ${LOGS_DAYS} 天)"
echo "  框架日志 plog : ${PLOG_DIR}   (> ${PLOG_DAYS} 天)"
echo "  执行结果      : ${OUTPUT_DIR}   (> ${OUTPUT_DAYS} 天)"
echo "  临时分支代码  : ${BASE_PATH}/sglang-{runid}   (> ${TEMP_DAYS} 天)"
echo

collect "执行日志" "$LOGS_DIR" "$LOGS_DAYS" "($RUN_DIR_RE)|($DATE_DIR_RE)"
collect "框架日志" "$PLOG_DIR" "$PLOG_DAYS" "($RUN_DIR_RE)|($DATE_DIR_RE)"
collect "执行结果" "$OUTPUT_DIR" "$OUTPUT_DAYS" "($RUN_DIR_RE)|($DATE_DIR_RE)"
collect "临时分支" "$BASE_PATH" "$TEMP_DAYS" "$TEMP_DIR_RE" "sglang-"

# 汇总（按删除候选数排序，只统计前 LIMIT 个的真实占用）
SORTED=()
mapfile -t SORTED < <(sort -n "$TMP_LIST")
TOTAL=${#SORTED[@]}
TARGET=$(( TOTAL < LIMIT ? TOTAL : LIMIT ))

# 统计各分类总大小（仅将要删除的那部分，避免全盘扫描）
for ((i = 0; i < TARGET; i++)); do
    IFS=$'\t' read -r _ category path <<< "${SORTED[$i]}"
    kb="$(du -sk -- "$path" 2>/dev/null | cut -f1)"
    SIZE_KB["$category"]=$(( ${SIZE_KB["$category"]:-0} + ${kb:-0} ))
done

days_for() {
    case "$1" in
        "执行日志") printf '%s' "$LOGS_DAYS" ;;
        "框架日志") printf '%s' "$PLOG_DAYS" ;;
        "执行结果") printf '%s' "$OUTPUT_DAYS" ;;
        *) printf '%s' "$TEMP_DAYS" ;;
    esac
}

# 按终端显示宽度左对齐补空格（中文按 2 列计），避免 printf %-Ns 在 CJK 下错位
pad() {
    local s="$1" want="$2" nb na w
    nb=$(printf '%s' "$s" | LC_ALL=C wc -c)
    na=$(printf '%s' "$s" | LC_ALL=C tr -d '\000-\177' | LC_ALL=C wc -c)
    w=$(( nb - na + (na / 3) * 2 ))
    printf '%s' "$s"
    if (( want > w )); then printf '%*s' $((want - w)) ''; fi
}

size_for() {
    awk -v k="${SIZE_KB[$1]:-0}" 'BEGIN{printf "%.1f GB", k/1024/1024}'
}

pad "分类" 12; pad "保留天数" 10; pad "待删除目录" 12; printf '%s\n' "本次释放"
pad "----" 12; pad "--------" 10; pad "----------" 12; printf '%s\n' "--------"
for name in "${ORDER[@]}"; do
    pad "$name" 12
    pad "$(days_for "$name") 天" 10
    pad "${CNT[$name]}" 12
    printf '%s\n' "$(size_for "$name")"
    if [[ "${SKIPPED[$name]:-0}" -gt 0 ]]; then
        printf '  └─ 另有 %s 个目录名字不符合预期格式，已跳过（不删除）\n' "${SKIPPED[$name]}"
    fi
done

echo
if (( TOTAL == 0 )); then
    echo "没有需要清理的目录。"
    exit 0
fi

echo "合计命中 ${TOTAL} 个目录，本次将删除 ${TARGET} 个（按最旧优先，单次上限 ${LIMIT}）。"
if (( TOTAL > LIMIT )); then
    echo "剩余 $((TOTAL - LIMIT)) 个请再次执行本脚本分批清理。"
fi

echo "前 10 个待删除目录（最旧优先）:"
for ((i = 0; i < TARGET && i < 10; i++)); do
    IFS=$'\t' read -r t category path <<< "${SORTED[$i]}"
    printf '  [%s] %s  (%s)\n' "$category" "$path" "$(date -d "@${t%.*}" '+%Y-%m-%d %H:%M' 2>/dev/null || echo '-')"
done

if (( DRY_RUN )); then
    echo
    echo "dry-run 模式，未删除任何目录。"
    exit 0
fi

if (( ! ASSUME_YES )); then
    echo
    # stdin 非终端（cron/CI/无输入）时 read 会失败，按“取消”处理而不是静默退出
    if [[ ! -t 0 ]]; then
        echo "stdin 不是交互终端，无法确认。请加 -y 直接删除，或用 --dry-run 只统计。"
        exit 1
    fi
    read -r -p "确认删除以上 ${TARGET} 个目录? [y/N] " ans || ans=""
    case "$ans" in
        y|Y|yes|YES) ;;
        *) echo "已取消，未删除任何目录。"; exit 0 ;;
    esac
fi

DELETED=0
FAILED=0
SKIPPED_OUT=0
for ((i = 0; i < TARGET; i++)); do
    IFS=$'\t' read -r _ category path <<< "${SORTED[$i]}"
    # 二次校验：必须是采集阶段记录的绝对路径，且位于所属分类根目录之下
    case "$category" in
        "执行日志") root="$LOGS_DIR"; re="($RUN_DIR_RE)|($DATE_DIR_RE)" ;;
        "框架日志") root="$PLOG_DIR"; re="($RUN_DIR_RE)|($DATE_DIR_RE)" ;;
        "执行结果") root="$OUTPUT_DIR"; re="($RUN_DIR_RE)|($DATE_DIR_RE)" ;;
        "临时分支") root="$BASE_PATH"; re="$TEMP_DIR_RE" ;;
        *) echo "WARN: 未知分类，跳过: ${category} (${path})" >&2; SKIPPED_OUT=$((SKIPPED_OUT + 1)); continue ;;
    esac
    base="${path##*/}"
    if [[ "$path" != /* || ! -d "$path" || "$path" == "$root" || "$path" != "$root"/* ]]; then
        SKIPPED_OUT=$((SKIPPED_OUT + 1))
        echo "WARN: 路径不在预期范围内，跳过: ${path}" >&2
        continue
    fi
    if [[ ! "$base" =~ $re ]]; then
        SKIPPED_OUT=$((SKIPPED_OUT + 1))
        echo "WARN: 目录名不符合预期格式，跳过: ${path}" >&2
        continue
    fi
    if rm -rf -- "$path"; then
        DELETED=$((DELETED + 1))
    else
        FAILED=$((FAILED + 1))
        echo "WARN: 删除失败: ${path}" >&2
    fi
done

echo
echo "已删除 ${DELETED} 个目录，失败 ${FAILED} 个。"
if (( SKIPPED_OUT > 0 )); then
    echo "另有 ${SKIPPED_OUT} 个目录因路径校验未通过被跳过，请人工确认。"
fi
if (( TOTAL > LIMIT )); then
    echo "仍有 $((TOTAL - LIMIT)) 个命中目录未处理，可再次执行。"
fi
