@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo [1/2] Killing existing dashboard processes...
for /f "tokens=2" %%a in ('tasklist ^| findstr /i "python" ^| findstr /i "dashboard"') do (
    echo   Killing PID %%a...
    taskkill /f /pid %%a 2>nul
)

echo [2/2] Starting dashboard...
start "" python dashboard.py

echo Done.
pause