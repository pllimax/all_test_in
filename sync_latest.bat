@echo off
rem 一键同步最新代码 - 双击运行
chcp 65001 >nul
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0sync_latest.ps1"
echo.
pause
