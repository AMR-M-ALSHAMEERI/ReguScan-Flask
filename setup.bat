@echo off
REM Setup script for ReguScan-Flask Application
REM This script sets up the environment and runs the application

echo ============================================
echo ReguScan-Flask Setup Script
echo ============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7 or higher from https://www.python.org/
    pause
    exit /b 1
)

echo [1/5] Python detected successfully
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo [2/5] Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
    echo Virtual environment created successfully
) else (
    echo [2/5] Virtual environment already exists
)
echo.

REM Activate virtual environment
echo [3/5] Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)
echo.

REM Install dependencies
echo [4/5] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo Dependencies installed successfully
echo.

REM Run the application
echo [5/5] Starting Flask application...
echo.
echo ============================================
echo Application is starting...
echo Open your browser and navigate to:
echo http://127.0.0.1:5000
echo.
echo Press Ctrl+C to stop the server
echo ============================================
echo.

python app.py
