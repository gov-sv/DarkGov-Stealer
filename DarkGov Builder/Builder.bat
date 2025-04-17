@echo off
cd /d %~dp0

title Checking libraries...
python -c "import customtkinter" > nul 2>&1
if %errorlevel% neq 0 (
    python -m pip install customtkinter > nul
)

python -c "import PIL" > nul 2>&1
if %errorlevel% neq 0 (
    python -m pip install pillow > nul
)

python -c "import pyaes" > nul 2>&1
if %errorlevel% neq 0 (.
    python -m pip install pyaesm > nul
)

python -c "import urllib3" > nul 2>&1
if %errorlevel% neq 0 (
    python -m pip install urllib3 > nul
)

cls
title Starting builder...
python gui.py
if %errorlevel% neq 0 goto ERROR
exit

:ERROR
color 4 && title [Error]
pause > nul