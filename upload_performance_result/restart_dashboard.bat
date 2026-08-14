@echo off
chcp 65001 >nul
cd /d "%~dp0"

rem GitHub Token for resolving GitHub Actions job links (Actions: Read scope)
rem Restart dashboard after modifying; replace with a new token if it expires.
rem NOTE: do not commit the real token to git. Fill it in locally only.
set "GH_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
set "GITHUB_TOKEN="

rem Notes git persistence interval in seconds (default 14400 = 4 hours)
rem Set to 0 to disable git persistence entirely.
set "NOTES_GIT_INTERVAL=14400"

echo [1/2] Killing existing dashboard processes...
rem tasklist only shows image names (no command line), so findstr "dashboard"
rem never matches. Use PowerShell to match python processes by command line.
powershell -NoProfile -Command "Get-CimInstance Win32_Process -Filter \"Name='python.exe'\" | Where-Object { $_.CommandLine -match 'dashboard\.py' } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue; Write-Host ('  Killed PID ' + $_.ProcessId) }"

echo [2/2] Starting dashboard...
rem NOTE: "start ... > file" redirects only apply to the start command itself,
rem NOT the child process. Use Start-Process -Redirect* to capture the
rem dashboard's output into log files in real time (python -u = unbuffered).
rem PYTHONUTF8=1: force UTF-8 output so Chinese text in dashboard.log is readable.
rem Use pythonw.exe (no console window) for fully background windowless run.
set "PYTHONUTF8=1"
rem stdout -> dashboard.log, stderr -> dashboard.err.log
powershell -NoProfile -Command "Start-Process -FilePath 'pythonw' -ArgumentList '-u','dashboard.py' -RedirectStandardOutput 'dashboard.log' -RedirectStandardError 'dashboard.err.log'"

echo Done.
pause
