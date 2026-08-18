#!/usr/bin/env bash

# 用法:
#   bash collect_metrics_cron.sh                      # 使用默认配置 collect_metrics_cron.conf
#   bash collect_metrics_cron.sh --config /path/conf  # 指定配置文件
#   bash collect_metrics_cron.sh --help               # 帮助
#
# 作用:
#   在 CI 机器上定期执行 collect_metrics.sh，收集指定分支（可多个）或指定日期的
#   用例执行结果并推送数据仓（upload_performance_result/metrics/sglang）。
#
# 特性:
#   - 支持多个分支:        COLLECT_BRANCHES="pllimax otherfork" 逐个收集
#   - 支持日期收集:        COLLECT_DATES="auto" 或 "20260818 20260817"（留空则不执行）
#   - 防重叠:              flock 加锁，上次执行未结束则本次跳过
#   - 代码保鲜:            每次执行前把所在仓库同步到远端 main（SYNC_CODE 可关闭）
#   - 统一日志:            时间戳日志写入 LOG_FILE，同时输出到终端；日志超限自动轮转
#   - 默认关闭多机日志:    COLLECT_LOGS=false，防止 CI 机器拷贝大日志超时
#
# 配置优先级: 脚本内置默认 < collect_metrics_cron.conf < 命令行 --config
# 敏感信息（如 GIT_TOKEN）建议放在 collect_metrics.local.conf（git-ignored），脚本会自动加载。

set -euo pipefail

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COLLECT_SCRIPT="${BASE_DIR}/collect_metrics.sh"
CONF="${CONF:-${BASE_DIR}/collect_metrics_cron.conf}"

# ---------- 内置默认配置（可被 conf 覆盖） ----------
# 要收集的分支前缀（空格分隔，可多个）；为空则跳过分支模式
COLLECT_BRANCHES=""
# 日期模式：auto=由本脚本计算今天及前3天并传入；或 "20260818 20260817"；为空则跳过日期模式
COLLECT_DATES=""
# 是否拉取多机用例完整日志（test_npu_*，量大耗时长易超时，定时任务建议 false）
COLLECT_LOGS="false"
# 每次执行前是否自动同步脚本代码（git fetch + reset --hard origin/main）
SYNC_CODE="true"
# 日志文件（时间戳日志与 collect_metrics.sh 输出均追加写入）
# 默认放用户可写目录：cron 常以非 root 运行，/var/log 通常无写权限，会导致定时日志全部丢失。
LOG_FILE="${LOG_FILE:-${HOME:-/tmp}/collect_metrics_cron.log}"
# 日志轮转阈值（字节，默认 20MB，超过后轮转为 ${LOG_FILE}.old）
LOG_MAX_SIZE="${LOG_MAX_SIZE:-20971520}"
# 防重叠锁文件
LOCK_FILE="/tmp/collect_metrics_cron.lock"

# ---------- 加载配置 ----------
if [ -f "${CONF}" ]; then
    # shellcheck disable=SC1090
    source "${CONF}"
fi

# ---------- 参数解析 ----------
while [[ $# -gt 0 ]]; do
    case $1 in
        --config)
            CONF="$2"
            shift 2
            if [ -f "${CONF}" ]; then
                # shellcheck disable=SC1090
                source "${CONF}"
            else
                echo "错误: 配置文件不存在: ${CONF}" >&2
                exit 1
            fi
            ;;
        -h|--help)
            sed -n '3,42p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'
            exit 0
            ;;
        *)
            echo "未知参数: $1（使用 --help 查看帮助）" >&2
            exit 1
            ;;
    esac
done

# ---------- 透传变量给 collect_metrics.sh ----------
# bash 中 source 的普通变量不会自动传给子进程；若不 export，子进程 collect_metrics.sh
# 会回落到内置默认值（如 GIT_REPO 默认 github 而非 gitee），导致推送错仓库。
# 此处显式 export 需透传的变量（未设置时 export 空值，子进程使用其内置默认，安全）。
export SRC_BASE LOG_BASE GIT_REPO GIT_TARGET_PATH GIT_LOCAL_DIR GIT_USER_NAME GIT_USER_EMAIL UPLOAD_RETRY UPLOAD_RETRY_DELAY UPLOAD_TIMEOUT

# ---------- 日志函数（写入 LOG_FILE + 输出到终端） ----------
_log() {
    local ts
    ts="[$(date '+%Y-%m-%d %H:%M:%S')]"
    echo "${ts} $*"
    echo "${ts} $*" >> "${LOG_FILE}" 2>/dev/null || true
}

# 日志轮转：超过 LOG_MAX_SIZE 字节时轮转为 ${LOG_FILE}.old
_rotate_log() {
    local size
    if [ -f "${LOG_FILE}" ]; then
        size=$(wc -c < "${LOG_FILE}" 2>/dev/null || echo 0)
        if [ "${size}" -gt "${LOG_MAX_SIZE}" ]; then
            mv -f "${LOG_FILE}" "${LOG_FILE}.old" 2>/dev/null || true
        fi
    fi
}

_rotate_log

# ---------- 1) 防重叠 ----------
exec 9>"${LOCK_FILE}"
if ! flock -n 9; then
    _log "已有实例在运行（${LOCK_FILE}），本次跳过"
    exit 0
fi

# ---------- 2) 代码保鲜（可选，默认开启） ----------
# 把脚本所在仓库同步到 origin/main，避免用旧逻辑/旧数据覆盖远端新提交。
# 同步前先 stash 本地修改（含未跟踪文件，如上次收集的缓存数据），同步后恢复，
# 避免 reset --hard 清掉本地未提交的改动。失败仅告警不中断。
if [ "${SYNC_CODE}" = "true" ] && git -C "${BASE_DIR}" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    if git -C "${BASE_DIR}" fetch origin --depth=1 2>/dev/null; then
        STASHED=false
        if [ -n "$(git -C "${BASE_DIR}" status --porcelain 2>/dev/null)" ]; then
            if git -C "${BASE_DIR}" stash push --include-untracked -m "collect_metrics_cron_auto_$(date +%Y%m%d%H%M%S)" 2>/dev/null; then
                STASHED=true
            fi
        fi
        if git -C "${BASE_DIR}" reset --hard origin/main 2>/dev/null; then
            _log "脚本代码已同步到 origin/main"
        else
            _log "[warn] reset --hard origin/main 失败，继续使用当前代码"
        fi
        if [ "${STASHED}" = true ]; then
            git -C "${BASE_DIR}" stash pop 2>/dev/null || _log "[warn] stash 恢复失败（可能冲突），请手动检查"
        fi
    else
        _log "[warn] git fetch 失败（网络问题？），继续使用当前代码"
    fi
fi

# ---------- 3) 执行收集 ----------
if [ ! -f "${COLLECT_SCRIPT}" ]; then
    _log "[error] 找不到 collect_metrics.sh: ${COLLECT_SCRIPT}"
    exit 1
fi

# 未配置任何收集项时直接告警退出，避免静默"完成"造成无数据却无感知
if [ -z "${COLLECT_BRANCHES}" ] && [ -z "${COLLECT_DATES}" ]; then
    _log "[error] 未配置任何收集项（COLLECT_BRANCHES / COLLECT_DATES 均为空），请检查 ${CONF}"
    exit 1
fi

if [ "${COLLECT_LOGS}" = "true" ]; then
    LOGS_FLAG="--collect-logs"
else
    LOGS_FLAG="--no-collect-logs"
fi

TOTAL_FAIL=0

# 3.1 分支模式（支持多个分支，逐个收集）
for b in ${COLLECT_BRANCHES}; do
    [ -n "${b}" ] || continue
    _log "==== 开始收集分支: ${b} ===="
    if "${COLLECT_SCRIPT}" --branch "${b}" ${LOGS_FLAG} >> "${LOG_FILE}" 2>&1; then
        _log "分支 ${b} 收集完成"
    else
        _log "[error] 分支 ${b} 收集失败（详见日志 ${LOG_FILE}）"
        TOTAL_FAIL=$((TOTAL_FAIL + 1))
    fi
done

# 3.2 日期模式（可选）：auto 由本脚本计算"今天及前3天"并显式传入，
# 因为 collect_metrics.sh 已取消内置自动模式，必须传显式日期。
if [ -n "${COLLECT_DATES}" ]; then
    if [ "${COLLECT_DATES}" = "auto" ]; then
        AUTO_DATES=()
        for i in 0 1 2 3; do
            d=$(date -d "$(date +%Y%m%d) - ${i} days" +%Y%m%d 2>/dev/null)
            [ -n "${d}" ] && AUTO_DATES+=("${d}")
        done
        _log "==== 开始收集日期: auto（今天及前3天: ${AUTO_DATES[*]}） ===="
        # shellcheck disable=SC2086
        if "${COLLECT_SCRIPT}" ${AUTO_DATES[*]} >> "${LOG_FILE}" 2>&1; then
            _log "日期模式(auto) 收集完成"
        else
            _log "[error] 日期模式(auto) 收集失败"
            TOTAL_FAIL=$((TOTAL_FAIL + 1))
        fi
    else
        _log "==== 开始收集日期: ${COLLECT_DATES} ===="
        # shellcheck disable=SC2086
        if "${COLLECT_SCRIPT}" ${COLLECT_DATES} >> "${LOG_FILE}" 2>&1; then
            _log "日期模式(${COLLECT_DATES}) 收集完成"
        else
            _log "[error] 日期模式(${COLLECT_DATES}) 收集失败"
            TOTAL_FAIL=$((TOTAL_FAIL + 1))
        fi
    fi
fi

if [ "${TOTAL_FAIL}" -gt 0 ]; then
    _log "[error] 本次 cron 执行共 ${TOTAL_FAIL} 项失败"
    exit 1
fi
_log "本次 cron 执行完成"
