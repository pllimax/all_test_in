#!/usr/bin/env bash
# ci_monitor 定时执行入口（供 cron / 手动调用）
# crontab 由 deploy.sh 自动安装，也可手动添加（北京时间 07:00）：
#   0 7 * * * /opt/all_test_in/historical_pr_parsing/run_ci_monitor.sh
set -uo pipefail

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$BASE_DIR"

# 优先使用 venv 中的 python
if [ -x "$BASE_DIR/venv/bin/python" ]; then
    PY="$BASE_DIR/venv/bin/python"
else
    PY=python3
fi

# 可选：从同目录 .env 读取凭据（GITHUB_TOKEN / AI_API_KEY / HTTPS_PROXY 等）
if [ -f "$BASE_DIR/.env" ]; then
    set -a
    # shellcheck disable=SC1091
    source "$BASE_DIR/.env"
    set +a
fi

mkdir -p "$BASE_DIR/logs"
LOG="$BASE_DIR/logs/ci_monitor_$(date +%Y%m%d).log"
exec >> "$LOG" 2>&1

# flock 防止上次未结束又启动
exec 9>"$BASE_DIR/ci_monitor.lock"
if ! flock -n 9; then
    echo "[$(date '+%F %T')] 上一次任务仍在运行，跳过本次"
    exit 0
fi

echo "[$(date '+%F %T')] NPU CI 监控启动"
"$PY" "$BASE_DIR/ci_monitor.py"
RC=$?
echo "[$(date '+%F %T')] NPU CI 监控结束, exit=$RC"
exit $RC
