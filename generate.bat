@echo off
REM Character generation batch file for CTchargen
REM This batch file provides a simple way to generate characters on Windows

echo CTchargen - Classic Traveller Character Generator
echo ================================================

if "%1"=="" (
    echo Generating 1 character with default settings...
    python generate_characters.py
) else (
    python generate_characters.py %*
)

echo.
echo Done!
pause
