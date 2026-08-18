#!/usr/bin/env bash
# ============================================================
# Gitee 数据仓 -> GitHub 数据仓 同步（文件级合并式，兼容无共同祖先）
#
# 背景:
#   - CI 机器把测试指标 push 到 Gitee 数据仓 (pllimax/all_test_in)
#   - 平台 dashboard 从 GitHub 数据仓读取指标，并把 notes.json 备注 push 到 GitHub
#   - 因此两端会分叉：不能用 --force 覆盖（会丢 GitHub 上的备注提交）
#   - Gitee 侧历史可能被 CI 的 --force-with-lease / force push 重写，
#     导致与 GitHub 无共同祖先（unrelated histories），git merge 会直接失败。
#
# 策略（自动降级）:
#   1) 两端有共同祖先 → 常规 merge（增量，保留双方历史）
#   2) merge 冲突 或 两端无共同祖先 → 文件级合并同步：
#      以 GitHub 为基准，把 Gitee 的指标数据目录（默认 metrics/sglang）
#      检出合并进来（只增/覆盖，不删除 GitHub 独有文件），再提交推送。
#
# 用法:
#   ./sync_gitee_to_github.sh                       # 使用本地配置/默认值
#   GITEE_TOKEN=xxx GITHUB_TOKEN=yyy ./sync_gitee_to_github.sh
#   WORK_DIR=/自定义/路径 ./sync_gitee_to_github.sh
#
# 定期同步（推荐用 install_sync_cron.sh 在远端服务器一键注册）:
#   cd /opt/all_test_in && bash install_sync_cron.sh      # 每 10 分钟同步一次
# 手动 crontab (Linux):
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
# 同步的数据路径（相对仓库根）。仅同步该路径，避免覆盖 GitHub 上平台维护的文件（notes.json 等）。
SYNC_PATH="${SYNC_PATH:-upload_performance_result/metrics/sglang}"

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
# 兼容 http:// 与 https:// 两种协议头（_strip_scheme 负责剥离）。
_strip_scheme() {
    local url="$1"
    case "$url" in
        http://*)  echo "${url#http://}" ;;
        https://*) echo "${url#https://}" ;;
        *)         echo "$url" ;;
    esac
}
if [ -n "$GITEE_TOKEN" ]; then
    GITEE_AUTH="https://oauth2:${GITEE_TOKEN}@$(_strip_scheme "$GITEE_REPO")"
else
    GITEE_AUTH="$GITEE_REPO"
fi
if [ -n "$GITHUB_TOKEN" ]; then
    GITHUB_AUTH="https://${GITHUB_TOKEN}@$(_strip_scheme "$GITHUB_REPO")"
else
    GITHUB_AUTH="$GITHUB_REPO"
fi

# 工作副本目录：指定目录不可写（如 Windows 上 /opt 不存在）时回退到用户目录
if ! mkdir -p "$WORK_DIR" 2>/dev/null; then
    WORK_DIR="${HOME:-/tmp}/.sync-gitee2github"
    mkdir -p "$WORK_DIR"
fi
cd "$WORK_DIR"

# 首次初始化：克隆 GitHub（含历史）；否则复用已有工作副本
if [ ! -d .git ]; then
    echo "[sync] 初始化：克隆 GitHub 数据仓..."
    git clone --no-checkout "$GITHUB_AUTH" .
fi

git remote set-url gitee "$GITEE_AUTH" 2>/dev/null || git remote add gitee "$GITEE_AUTH"
git remote set-url github "$GITHUB_AUTH" 2>/dev/null || git remote add github "$GITHUB_AUTH"

# 文件级合并同步：以当前 HEAD（GitHub 基准）为底，把 Gitee 的 SYNC_PATH
# 检出覆盖/新增进来（git checkout <tree> -- <path> 只增与覆盖，不删除本地独有文件），
# 再提交。该方式不依赖两端共同祖先，可处理 force push 导致的 unrelated histories。
# SYNC_PATH 支持空格分隔的多个相对路径，逐个处理。
_file_level_sync() {
    local p sync_any=0
    for p in ${SYNC_PATH}; do
        [ -n "$p" ] || continue
        if ! git cat-file -e "gitee/$BRANCH:$p" 2>/dev/null; then
            echo "[sync] 警告: Gitee 上不存在路径 ${p}，跳过"
            continue
        fi
        git checkout "gitee/$BRANCH" -- "$p"
        sync_any=1
    done
    if [ "${sync_any}" -eq 0 ]; then
        echo "[sync] 警告: Gitee 上不存在任何 SYNC_PATH（${SYNC_PATH}），跳过文件级同步"
        return 0
    fi
    git add -A
    if git diff --cached --quiet; then
        echo "[sync] ${SYNC_PATH} 无变更，跳过提交"
    else
        git commit -m "sync: 从 gitee 文件级合并 ${SYNC_PATH} - $(date +%Y%m%d)"
    fi
}

echo "[sync] fetch gitee/$BRANCH"
git fetch gitee "$BRANCH"
echo "[sync] fetch github/$BRANCH"
git fetch github "$BRANCH"

echo "[sync] 以 GitHub 为基准，合并 Gitee 更新"
git checkout -B "$BRANCH" "github/$BRANCH"

# 判断两端是否有共同祖先（Gitee 可能被 force push 重写 → unrelated histories）
if git merge-base "github/$BRANCH" "gitee/$BRANCH" >/dev/null 2>&1; then
    echo "[sync] 两端有共同祖先，尝试常规 merge"
    if git merge --no-edit "gitee/$BRANCH"; then
        :
    else
        echo "[sync] merge 冲突，改用文件级合并同步 ${SYNC_PATH}..."
        git merge --abort 2>/dev/null || true
        git checkout -f "github/$BRANCH"
        _file_level_sync
    fi
else
    echo "[sync] 两端历史不相关（可能被 force push 重写），使用文件级合并同步 ${SYNC_PATH}"
    _file_level_sync
fi

# 推送（带冲突降级）：
#   1) 直接 push；
#   2) 被拒（平台可能刚推了备注）→ pull 追平远端后重试；
#   3) pull 冲突或再次被拒 → 回到文件级合并（只同步 SYNC_PATH，不覆盖平台维护文件）后重推。
echo "[sync] push github/$BRANCH"
if git push github "$BRANCH"; then
    :
elif git pull --no-rebase --no-edit github "$BRANCH" && git push github "$BRANCH"; then
    :
else
    echo "[sync] push 冲突，改用文件级合并 ${SYNC_PATH} 后重试"
    git merge --abort 2>/dev/null || true
    git checkout -f "github/$BRANCH"
    _file_level_sync
    git push github "$BRANCH"
fi

echo "[sync] 完成: $(git rev-parse --short HEAD)"
