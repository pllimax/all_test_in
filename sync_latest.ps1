<#
    一键同步最新代码 (Windows PowerShell)

    功能：
      1. 启用 git 长路径支持（core.longpaths）
      2. 拉取远端 main 最新提交
      3. 检测本地是否有未提交改动/未跟踪文件，有则先 stash 暂存（保留本地改动），同步后再恢复
      4. 将本地工作区强制同步到远端最新（reset --hard origin/main）

    用法：
      - 双击运行（需配合 sync_latest.bat）
      - 或命令行：powershell -NoProfile -ExecutionPolicy Bypass -File .\sync_latest.ps1
      可选参数：-Force 跳过确认，直接同步（本地改动仍会暂存并保留）
#>
param(
    [switch]$Force
)

$ErrorActionPreference = 'Stop'
$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $Root

function Fail($msg) {
    Write-Host "[错误] $msg" -ForegroundColor Red
    exit 1
}

Write-Host "== 1/3 启用 git 长路径支持 ==" -ForegroundColor Cyan
git config core.longpaths true
if ($LASTEXITCODE -ne 0) { Fail "设置 core.longpaths 失败" }

Write-Host "== 2/3 拉取远端最新 ==" -ForegroundColor Cyan
git fetch origin main
if ($LASTEXITCODE -ne 0) { Fail "git fetch 失败，请检查网络/凭据" }

Write-Host "== 3/3 同步工作区到远端最新 ==" -ForegroundColor Cyan
# 检查是否有未提交改动或未跟踪文件
$dirty = git status --porcelain
$stashed = $false
if ($dirty) {
    Write-Host "检测到本地存在未提交改动/未跟踪文件：将先暂存(stash)再同步，同步完成后恢复，保留本地改动。"
    Write-Host $dirty
    if (-not $Force) {
        Write-Host ""
        Write-Host "是否继续？本地改动会被暂存并在同步后恢复。 [y/N] " -NoNewline
        $ans = Read-Host
        if ($ans -notmatch '^[yY]') { Write-Host "已取消同步。" -ForegroundColor Yellow; exit 1 }
    }
    # 暂存本地改动（含未跟踪文件），保留到 stash 列表；git-ignored 文件（如 collect_metrics.local.conf）不受影响
    git stash push -u -m "sync_latest: 同步前暂存本地改动"
    if ($LASTEXITCODE -ne 0) { Fail "暂存本地改动失败" }
    $stashed = $true
}

git reset --hard origin/main
if ($LASTEXITCODE -ne 0) { Fail "同步到远端最新失败" }

# 同步完成后恢复暂存的本地改动
if ($stashed) {
    Write-Host "恢复本地暂存的改动..."
    git stash pop
    if ($LASTEXITCODE -ne 0) {
        Write-Host "警告: 恢复本地改动时出现冲突，冲突内容仍保留在 stash 中，请手动解决。" -ForegroundColor Yellow
        Write-Host "可执行: git stash list 查看，git stash pop 重新恢复。" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "已同步到最新提交: " -ForegroundColor Green -NoNewline
git log -1 --oneline
Write-Host "完成！" -ForegroundColor Green
