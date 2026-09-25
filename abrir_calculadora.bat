@echo off
cd /d "%~dp0"
pythonw interface\calculadora.py
if errorlevel 1 (
    echo.
    echo Nao foi possivel abrir a calculadora.
    echo Verifique se o Python esta instalado e se o numpy esta instalado.
    pause
)
