@echo off
echo Starting Health Chatbot...
echo.

echo Starting Backend Server...
start "Backend" cmd /k "cd health-chatbot-backend && python main.py"

echo Waiting 3 seconds for backend to start...
timeout /t 3 /nobreak > nul

echo Starting Frontend Server...
start "Frontend" cmd /k "cd health-chatbot-frontend && npm start"

echo.
echo Both servers are starting...
echo Backend: http://localhost:8000
echo Frontend: http://localhost:3000
echo.
pause