@echo off
rem One-click sync latest code. Double-click to run.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0sync_latest.ps1"
echo.
pause
