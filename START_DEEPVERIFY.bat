@echo off
echo ========================================
echo  DeepVerify GitHub Gold Miner
echo  Baslatiliyor...
echo ========================================
echo.

REM Check if Python is installed
py --version >nul 2>&1
if errorlevel 1 (
    echo [HATA] Python bulunamadi!
    echo Lutfen Python yukleyin: https://python.org
    pause
    exit /b 1
)

REM Install required packages
echo [1/3] Gerekli paketler kontrol ediliyor...
py -m pip install flask flask-cors >nul 2>&1

REM Start the server
echo [2/3] Server baslatiliyor...
start "DeepVerify Server" py deepverify_server.py

REM Wait a bit for server to start
timeout /t 3 /nobreak >nul

REM Open the web interface
echo [3/3] Web arayuzu aciliyor...
start "" "index.html"

echo.
echo ========================================
echo  DeepVerify basariyla baslatildi!
echo ========================================
echo.
echo  Web Arayuzu: deepverify-github-miner.html
echo  Server: http://localhost:5000
echo.
echo  Server'i durdurmak icin server penceresini kapatin
echo.
pause
