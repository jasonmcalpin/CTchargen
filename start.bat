@echo off
echo Starting CTchargen application...

REM Activate virtual environment
call .\venv\Scripts\activate

REM Start the backend server in a new window
start "CTchargen Backend" cmd /c "python scripts\run_backend.py"

REM Wait for the backend to start
echo Waiting for backend server to start...
timeout /t 5 /nobreak > nul

REM Start the frontend server in a new window
start "CTchargen Frontend" cmd /c "python scripts\run_frontend.py"

REM Wait for the frontend to start
echo Waiting for frontend server to start...
timeout /t 10 /nobreak > nul

REM Open the web interface in the default browser
echo Opening web interface in browser...
start http://localhost:3000

echo CTchargen application started successfully!
echo.
echo To stop the application, close the backend and frontend terminal windows.
echo.
pause
