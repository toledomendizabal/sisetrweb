@echo off
REM ============================================================================
REM SISETRWEB - Script de Inicio del Bot (Mejorado)
REM ============================================================================
REM Este script inicia el bot SISETRWEB correctamente
REM Uso: Ejecutar desde PowerShell o CMD
REM ============================================================================

setlocal enabledelayedexpansion

cls

echo.
echo ============================================================================
echo SISETRWEB - Iniciando Bot de Trading Autogestionado
echo ============================================================================
echo.

REM Verificar que Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no está instalado o no está en el PATH
    pause
    exit /b 1
)

REM Verificar que estamos en la carpeta correcta
if not exist "src\main.py" (
    echo ERROR: No se encontró src\main.py
    echo Asegúrate de estar en la carpeta correcta: C:\xampp\htdocs\sisetrweb
    pause
    exit /b 1
)

REM Verificar que el entorno virtual existe
if not exist "venv\Scripts\activate.bat" (
    echo ERROR: No se encontró el entorno virtual
    echo Ejecuta primero: python -m venv venv
    pause
    exit /b 1
)

echo [✓] Verificaciones previas completadas
echo.

REM Activar el entorno virtual
echo Activando entorno virtual...
call venv\Scripts\activate.bat

if errorlevel 1 (
    echo ERROR: No se pudo activar el entorno virtual
    pause
    exit /b 1
)

echo [✓] Entorno virtual activado
echo.

REM Ejecutar el bot
echo Iniciando SISETRWEB...
echo.

REM Opción 1: Ejecutar con el script boot.py (RECOMENDADO)
if exist "boot.py" (
    echo Ejecutando: python boot.py
    python boot.py
    goto end
)

REM Opción 2: Ejecutar como módulo
echo Ejecutando: python -m src
python -m src
goto end

:end
echo.
echo ============================================================================
echo Bot detenido
echo ============================================================================
echo.
pause
