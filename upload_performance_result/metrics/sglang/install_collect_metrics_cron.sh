#!/usr/bin/env bash

# 用法:
#   bash install_collect_metrics_cron.sh                                   # 默认每小时执行一次
#   bash install_collect_metrics_cron.sh --interval '*/30 * * * *'          # 每30分钟
#   bash install_collect_metrics_cron.sh --config /path/collect_metrics_cron.conf
#   bash install_collect_metrics_cron.sh --no-first-run                    # 不立即执行验证
#
# 作用:
#   在 CI 机器上一键注册 collect_metrics_cron.sh 的 crontab 定时任务，
#   默认每小时第0分钟执行一次；并默认首次立即执行一次做验证。
#   重复执行会先移除旧任务再注册，不会叠加。

set -euo pipefail

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CRON_SCRIPT="${BASE_DIR}/collect_metrics_cron.sh"
CONF=""
# 默认每小时执行（第0分钟）；可用 --interval 覆盖（cron 5 段表达式）
INTERVAL="0 * * * *"
FIRST_RUN="true"

while [[ $# -gt 0 ]]; do
    case $1 in
        --interval)   INTERVAL="$2"; shift 2 ;;
        --config)     CONF="$2"; shift 2 ;;
        --no-first-run) FIRST_RUN="false"; shift ;;
        -h|--help)
            echo "用法: bash $0 [--interval '0 * * * *'] [--config /path/conf] [--no-first-run]"
            exit 0
            ;;
        *)
            echo "未知参数: $1" >&2
            exit 1
            ;;
    esac
done

if [ ! -f "${CRON_SCRIPT}" ]; then
    echo "错误: 找不到 ${CRON_SCRIPT}" >&2
    exit 1
fi
chmod +x "${CRON_SCRIPT}" 2>/dev/null || true

# 组装 cron 命令行（含可选 --config）。
# 脚本内部已自写日志（LOG_FILE，默认用户目录），cron 行不再重定向到同一文件，
# 避免与脚本内 _log 双写导致日志重复；stdout/stderr 丢弃，也避免非 root 写 /var/log 失败。
CRON_ARGS=""
if [ -n "${CONF}" ]; then
    CRON_ARGS="--config ${CONF}"
fi
CRON_LINE="${INTERVAL} /bin/bash ${CRON_SCRIPT} ${CRON_ARGS} >/dev/null 2>&1"

# 移除已存在的 collect_metrics_cron 任务（防重复注册）
(crontab -l 2>/dev/null || true) | grep -v "collect_metrics_cron.sh" | crontab -

# 注册新任务
{
    crontab -l 2>/dev/null || true
    echo "${CRON_LINE}"
} | crontab -

echo "已注册 crontab 任务:"
echo "  ${CRON_LINE}"
echo "当前任务列表:"
crontab -l | grep "collect_metrics_cron.sh" || true

# 首次立即执行验证（默认开启；--no-first-run 可跳过）。
# 验证失败仅告警不中断：crontab 任务已注册成功，避免误判为注册失败。
if [ "${FIRST_RUN}" = "true" ]; then
    echo ""
    echo "========== 首次立即执行验证 =========="
    if /bin/bash "${CRON_SCRIPT}" ${CRON_ARGS}; then
        echo "首次执行验证成功"
    else
        echo "警告: 首次执行验证失败（crontab 任务已注册，请按下方命令查看日志排查）"
    fi
    echo "======================================"
fi

echo ""
echo "完成。常用排查:"
echo "  查看任务:   crontab -l | grep collect_metrics_cron"
echo "  查看日志:   tail -f ~/collect_metrics_cron.log（若在配置中自定义了 LOG_FILE 则查看对应路径）"
