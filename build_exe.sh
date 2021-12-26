#!/bin/bash
if pip3 show pyinstaller &> /dev/null; then
  pyinstaller --clean --onefile --icon=logo.ico main.py
else
  pip install pyinstaller
fi