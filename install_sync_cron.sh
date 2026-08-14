#!/usr/bin/env bash
# ============================================================
# 远端服务器安装脚本：注册 Gitee -> GitHub 定期同步 crontab
#
# 用法（在远端服务器上，仓库已同步到 /opt/all_test_in）:
#   cd /opt/all_test_in && bash install_sync_cron.sh
#   # 或指定仓库路径: bash install_sync_cron.sh /path/to/all_test_in
#
# 功能:
#   1. 校验 sync_gitee_to_github.sh 与 conf 是否存在
#   2. 追加/更新 crontab 定时任务（默认每 10 分钟一次）
#   3. 首次运行时立即执行一次同步，验证配置
#
# 依赖: crontab 命令；远端需能同时访问 Gitee 与 GitHub。
# ============================================================
set -euo pipefail

REPO_DIR="${1:-$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)}"
SCRIPT="$REPO_DIR/sync_gitee_to_github.sh"
CONF="$REPO_DIR/sync_gitee_to_github.conf"
LOG="/var/log/sync_gitee_to_github.log"
# 同步频率（分钟）
INTERVAL_MIN="${INTERVAL_MIN:-10}"

# ---- 校验 ----
if [ ! -f "$SCRIPT" ]; then
    echo "[install] 错误: 未找到同步脚本 $SCRIPT" >&2
    exit 1
fi
if [ ! -f "$CONF" ]; then
    echo "[install] 警告: 未找到 $CONF（token 配置），将按公开 HTTPS 直连。" >&2
    echo "[install] 如需推送私有仓，请先复制 sync_gitee_to_github.conf.example 为 conf 并填入 token。" >&2
fi
if ! command -v crontab >/dev/null 2>&1; then
    echo "[install] 错误: 未安装 crontab（cron 服务）" >&2
    exit 1
fi
# 确保脚本可执行
chmod +x "$SCRIPT" 2>/dev/null || true

# ---- 生成 crontab 行 ----
CRON_LINE="*/${INTERVAL_MIN} * * * * ${SCRIPT} >> ${LOG} 2>&1"

# 移除旧的同任务行（避免重复），再追加
crontab -l 2>/dev/null | grep -v "sync_gitee_to_github.sh" > "${TMPDIR:-/tmp}/cron_new.$$" || true
echo "$CRON_LINE" >> "${TMPDIR:-/tmp}/cron_new.$$"
crontab "${TMPDIR:-/tmp}/cron_new.$$"
rm -f "${TMPDIR:-/tmp}/cron_new.$$"

echo "[install] 已注册 crontab（每 ${INTERVAL_MIN} 分钟）:"
echo "    $CRON_LINE"
echo "[install] 日志: $LOG"
echo ""

# ---- 首次立即执行，验证配置 ----
echo "[install] 立即执行一次同步验证..."
if bash "$SCRIPT"; then
    echo "[install] 验证成功：首次同步完成。"
else
    echo "[install] 警告: 首次同步未完全成功，请检查上面的输出与 $LOG。" >&2
fi

echo ""
echo "[install] 完成。查看任务: crontab -l | grep sync_gitee_to_github"
echo "[install] 手动同步: bash $SCRIPT"
