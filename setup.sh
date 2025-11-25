#!/bin/bash
# Setup script for ReguScan-Flask Application (macOS/Linux)
# This script sets up the environment and runs the application

echo "============================================"
echo "ReguScan-Flask Setup Script"
echo "============================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.7 or higher"
    exit 1
fi

echo "[1/5] Python detected successfully"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "[2/5] Creating virtual environment..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to create virtual environment"
        exit 1
    fi
    echo "Virtual environment created successfully"
else
    echo "[2/5] Virtual environment already exists"
fi
echo ""

# Activate virtual environment
echo "[3/5] Activating virtual environment..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to activate virtual environment"
    exit 1
fi
echo ""

# Install dependencies
echo "[4/5] Installing dependencies..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi
echo "Dependencies installed successfully"
echo ""

# Run the application
echo "[5/5] Starting Flask application..."
echo ""
echo "============================================"
echo "Application is starting..."
echo "Open your browser and navigate to:"
echo "http://127.0.0.1:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo "============================================"
echo ""

python3 app.py
