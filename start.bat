@echo off
title NewsWeave

echo ============================================
echo   NewsWeave - Iniciando servicos...
echo ============================================
echo.

:: Mata processos anteriores nas portas
for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":8001 "') do (
    if not "%%a"=="0" taskkill /f /pid %%a >nul 2>&1
)
for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":3000 "') do (
    if not "%%a"=="0" taskkill /f /pid %%a >nul 2>&1
)
timeout /t 2 /nobreak >nul

:: Backend
echo [1/3] Iniciando backend (porta 8001)...
start "NewsWeave-Backend" cmd /c "cd /d "%~dp0backend" && python -m uvicorn app.main:app --host 127.0.0.1 --port 8001 --reload"
timeout /t 5 /nobreak >nul

:: Frontend
echo [2/3] Iniciando frontend (porta 3000)...
start "NewsWeave-Frontend" cmd /c "cd /d "%~dp0frontend" && npm run dev"
timeout /t 8 /nobreak >nul

:: Browser
echo [3/3] Abrindo navegador...
start http://localhost:3000

echo.
echo ============================================
echo   NewsWeave rodando!
echo   Frontend: http://localhost:3000
echo   Backend:  http://localhost:8001
echo.
echo   Feche esta janela para parar tudo.
echo ============================================
echo.
pause >nul

:: Fecha processos ao fechar
taskkill /fi "WINDOWTITLE eq NewsWeave-Backend" /f >nul 2>&1
taskkill /fi "WINDOWTITLE eq NewsWeave-Frontend" /f >nul 2>&1
