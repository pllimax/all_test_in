#!/usr/bin/env bash
# ============================================================
# Gitee 数据仓 -> GitHub 数据仓 单向同步（合并式）
#
# 背景:
#   - CI 机器把测试指标 push 到 Gitee 数据仓 (pllimax/all_test_in)
#   - 平台 dashboard 从 GitHub 数据仓读取指标，并把 notes.json 备注 push 到 GitHub
#   - 因此两端会分叉：不能用 --force 覆盖（会丢 GitHub 上的备注提交）
#   - 本脚本以 GitHub 为基准，把 Gitee 的更新 merge 进来再 push 回 GitHub
#
# 用法:
#   ./sync_gitee_to_github.sh                       # 使用本地配置/默认值
#   GITEE_TOKEN=xxx GITHUB_TOKEN=yyy ./sync_gitee_to_github.sh
#   WORK_DIR=/自定义/路径 ./sync_gitee_to_github.sh
#
# 定时执行 (crontab -e):
#   */10 * * * * /opt/all_test_in/sync_gitee_to_github.sh >> /var/log/sync_gitee_to_github.log 2>&1
#
# 依赖: bash + git；运行机器需能同时访问 Gitee 与 GitHub。
# ============================================================
set -euo pipefail

# ---- 默认值（可被环境变量 / 本地配置文件覆盖） ----
GITEE_REPO="${GITEE_REPO:-https://gitee.com/pllimax/all_test_in.git}"
GITHUB_REPO="${GITHUB_REPO:-https://github.com/pllimax/all_test_in.git}"
BRANCH="${BRANCH:-main}"
WORK_DIR="${WORK_DIR:-/opt/sync-gitee2github}"
GITEE_TOKEN="${GITEE_TOKEN:-}"
GITHUB_TOKEN="${GITHUB_TOKEN:-}"

# 本地覆盖配置（git-ignored，可安全存放 token）
_SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
_CONF="${_SCRIPT_DIR}/sync_gitee_to_github.conf"
if [ -f "$_CONF" ]; then
    # shellcheck disable=SC1090
    source "$_CONF"
fi

# 构造带认证地址
# Gitee: oauth2:TOKEN@gitee.com（已验证）
# GitHub: TOKEN@github.com（GitHub 接受以 token 作为用户名的形式）
if [ -n "$GITEE_TOKEN" ]; then
    GITEE_AUTH="https://oauth2:${GITEE_TOKEN}@${GITEE_REPO#https://}"
else
    GITEE_AUTH="$GITEE_REPO"
fi
if [ -n "$GITHUB_TOKEN" ]; then
    GITHUB_AUTH="https://${GITHUB_TOKEN}@${GITHUB_REPO#https://}"
else
    GITHUB_AUTH="$GITHUB_REPO"
fi

mkdir -p "$WORK_DIR"
cd "$WORK_DIR"

# 首次初始化：克隆 GitHub（含历史）；否则复用已有工作副本
if [ ! -d .git ]; then
    echo "[sync] 初始化：克隆 GitHub 数据仓..."
    git clone --no-checkout "$GITHUB_AUTH" .
fi

git remote set-url gitee "$GITEE_AUTH" 2>/dev/null || git remote add gitee "$GITEE_AUTH"
git remote set-url github "$GITHUB_AUTH" 2>/dev/null || git remote add github "$GITHUB_AUTH"

echo "[sync] fetch gitee/$BRANCH"
git fetch gitee "$BRANCH"
echo "[sync] fetch github/$BRANCH"
git fetch github "$BRANCH"

echo "[sync] 以 GitHub 为基准，合并 Gitee 更新"
git checkout -B "$BRANCH" "github/$BRANCH"
if ! git merge --no-edit "gitee/$BRANCH"; then
    echo "[sync] 合并冲突，请手动处理: git -C $WORK_DIR status" >&2
    exit 1
fi

echo "[sync] push github/$BRANCH"
if ! git push github "$BRANCH"; then
    echo "[sync] push 被拒（平台可能刚推了备注），合并远端最新后重试"
    git pull --no-rebase --no-edit github "$BRANCH"
    git push github "$BRANCH"
fi

echo "[sync] 完成: $(git rev-parse --short HEAD)"
