<#
    一键同步最新代码 (Windows PowerShell)

    功能：
      1. 启用 git 长路径支持（core.longpaths）
      2. 拉取远端 main 最新提交
      3. 检测本地是否有未提交改动/未跟踪文件，如会阻塞同步则提示确认后清理
      4. 将本地工作区强制同步到远端最新（reset --hard origin/main）

    用法：
      - 双击运行（需配合 sync_latest.bat）
      - 或命令行：powershell -NoProfile -ExecutionPolicy Bypass -File .\sync_latest.ps1
      可选参数：-Force 跳过清理确认，直接同步
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
if ($dirty) {
    Write-Host "检测到本地存在未提交改动/未跟踪文件（会阻塞同步）："
    Write-Host $dirty
    if (-not $Force) {
        Write-Host ""
        Write-Host "是否强制同步到远端最新？将丢弃上述本地改动/未跟踪文件。 [y/N] " -NoNewline
        $ans = Read-Host
        if ($ans -notmatch '^[yY]') { Write-Host "已取消同步。" -ForegroundColor Yellow; exit 1 }
    }
    # 丢弃本地改动
    git reset --hard HEAD; if ($LASTEXITCODE -ne 0) { Fail "reset 本地改动失败" }
    # 删除会与远端冲突的未跟踪文件/目录（保留 git-ignored 文件，如 collect_metrics.local.conf）
    git clean -fd; if ($LASTEXITCODE -ne 0) { Fail "清理未跟踪文件失败" }
}

git reset --hard origin/main
if ($LASTEXITCODE -ne 0) { Fail "同步到远端最新失败" }

Write-Host ""
Write-Host "已同步到最新提交: " -ForegroundColor Green -NoNewline
git log -1 --oneline
Write-Host "完成！" -ForegroundColor Green
