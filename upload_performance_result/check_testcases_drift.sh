#!/bin/bash
# nightly 用例配置漂移检测 cron 包装：固定工作目录与日志，供 crontab 调用。
# 建议 crontab 条目（每日 08:30）：
#   30 8 * * * /bin/bash /opt/sglang-dashboard/all_test_in_main/upload_performance_result/check_testcases_drift.sh >> /opt/sglang-dashboard/all_test_in_main/logs/testcases_drift/cron.log 2>&1
set -u
BASE="$(cd "$(dirname "$0")" && pwd)"
REPO="$(dirname "$BASE")"
mkdir -p "$REPO/logs/testcases_drift"
exec /usr/bin/python3 "$BASE/check_testcases_drift.py" --repo-dir "$BASE/.testcases_repo/nightly"
