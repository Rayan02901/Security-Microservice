@echo off
title Security Microservice - Dev

cd /d "%~dp0"

echo ================================
echo Starting Dev Environment
echo ================================

echo Installing dependencies...
python -m pip install --upgrade pip
IF ERRORLEVEL 1 goto error

pip install -r requirements.txt
IF ERRORLEVEL 1 goto error

echo Running unit tests...
python -m pytest -v
IF ERRORLEVEL 1 goto error

echo Tests passed. Starting application...

set APP_ENV=dev
uvicorn app.main:app --reload
goto end

:error
echo.
echo ❌ An error occurred. See messages above.
pause

:end
