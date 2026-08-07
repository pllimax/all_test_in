@echo off
chcp 65001 >nul
cd /d "%~dp0"

rem GitHub Token：用于解析 GitHub Actions job 级任务链接（Actions: Read 权限）
rem 修改后需重启 dashboard 生效；如失效可替换为新的 token
rem 注意：请勿将真实 token 提交到 git，本地使用时可在此填写
set "GH_TOKEN="
set "GITHUB_TOKEN="

echo [1/2] Killing existing dashboard processes...
for /f "tokens=2" %%a in ('tasklist ^| findstr /i "python" ^| findstr /i "dashboard"') do (
    echo   Killing PID %%a...
    taskkill /f /pid %%a 2>nul
)

echo [2/2] Starting dashboard...
start "" python dashboard.py

echo Done.
pause