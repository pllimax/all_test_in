#!/usr/bin/env bash
# historical_pr_parsing 一键部署：venv + 依赖 + cron（幂等，可重复执行）
set -euo pipefail

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$BASE_DIR"

# 1. Python venv + 依赖
if [ ! -x venv/bin/python ]; then
    echo "[deploy] 创建 venv..."
    python3 -m venv venv
fi
echo "[deploy] 安装依赖..."
./venv/bin/pip install --quiet --disable-pip-version-check requests urllib3

# 2. crontab：自动按服务器时区换算到北京时间 07:00（幂等：先删旧条目）
echo "[deploy] 安装 crontab..."
if [ "$(date +%z)" = "+0800" ]; then
    CRON_LINE="0 7 * * * $BASE_DIR/run_ci_monitor.sh"
else
    CRON_LINE="0 23 * * * $BASE_DIR/run_ci_monitor.sh"
fi
( crontab -l 2>/dev/null | grep -v "historical_pr_parsing_ci_monitor" || true
  echo "$CRON_LINE historical_pr_parsing_ci_monitor" ) | crontab -
echo "[deploy] cron 已安装: $CRON_LINE"

# 3. 连通性自检
echo "[deploy] 连通性检查..."
"$BASE_DIR/venv/bin/python" - <<'EOF'
import os, requests, urllib3
urllib3.disable_warnings()
gh = requests.get("https://api.github.com/rate_limit",
                  headers={"Authorization": f"Bearer {os.environ.get('GITHUB_TOKEN','')}"},
                  verify=False, timeout=15)
print(f"  github api: HTTP {gh.status_code}")
ds = requests.get("https://api.deepseek.com", verify=False, timeout=15)
print(f"  deepseek api: HTTP {ds.status_code}")
EOF

echo "[deploy] 部署完成。手动试跑: $BASE_DIR/run_ci_monitor.sh ; 日志: $BASE_DIR/logs/"
