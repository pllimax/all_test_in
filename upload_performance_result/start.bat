@echo off
echo ============================================
echo  SGLang Performance Analysis Platform
echo ============================================
echo.

REM Step 1: Install Python dependencies
echo [1/3] Installing Python dependencies...
pip install -r requirements.txt -q
echo.

REM Step 2: Start Prometheus Exporter (background)
echo [2/3] Starting Prometheus Exporter on port 9099...
start "SGLang-Exporter" cmd /c "python prometheus_exporter.py"
echo.

REM Step 3: Start Docker containers
echo [3/3] Starting Prometheus + Grafana via Docker...
docker-compose up -d
echo.

echo ============================================
echo  Platform is starting up!
echo.
echo  Prometheus:  http://localhost:9090
echo  Grafana:     http://localhost:3000  (admin/admin)
echo  Exporter:    http://localhost:9099/metrics
echo.
echo  Dashboard: Grafana -> Dashboards -> SGLang Benchmark
echo ============================================
pause
