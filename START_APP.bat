@echo off
title Construction Cost Predictor
echo ==========================================
echo   Construction Cost & Delay Predictor
echo ==========================================
echo.
echo Starting the application...
echo.
cd /d "C:\Users\arshi\Desktop\project 2\construction_predictor"
echo Opening browser in 3 seconds...
timeout /t 3 /nobreak >nul
start http://127.0.0.1:5000
python run.py
pause
