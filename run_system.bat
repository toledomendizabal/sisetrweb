@echo off
title SISETRWEB Bot - Sistema de Trading Autogestionado
echo ======================================================
echo   Iniciando SISETRWEB Bot...
echo ======================================================

:: Verificar si Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python no está instalado o no está en el PATH.
    pause
    exit /b
)

:: Verificar si el entorno virtual existe, si no, crearlo
if not exist "venv" (
    echo Creando entorno virtual...
    python -m venv venv
)

:: Activar entorno virtual e instalar dependencias
echo Activando entorno virtual e instalando dependencias...
call venv\Scripts\activate
pip install -r requirements.txt

:: Iniciar el bot
echo Iniciando el motor principal y el dashboard...
python src/main.py

pause
