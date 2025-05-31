@echo off
echo Fixing frontend build issues...
call .\venv\Scripts\activate
python scripts\fix_frontend_build.py
pause
