@echo off
REM ============================================================================
REM SISETRWEB - Script de Instalación Automática para Windows
REM ============================================================================
REM Este script automatiza la instalación de todas las dependencias del bot
REM Uso: Ejecutar este archivo desde PowerShell o CMD
REM ============================================================================

setlocal enabledelayedexpansion
cls

echo.
echo ============================================================================
echo SISETRWEB - Instalador Automático para Windows
echo ============================================================================
echo.

REM Verificar que Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no está instalado o no está en el PATH
    echo Descarga Python 3.11+ desde https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [✓] Python detectado
python --version

echo.
echo ============================================================================
echo PASO 1: Actualizar pip, setuptools y wheel
echo ============================================================================
echo.

python -m pip install --upgrade pip setuptools wheel

if errorlevel 1 (
    echo ERROR: No se pudo actualizar pip
    pause
    exit /b 1
)

echo [✓] pip, setuptools y wheel actualizados

echo.
echo ============================================================================
echo PASO 2: Crear entorno virtual (si no existe)
echo ============================================================================
echo.

if not exist "venv" (
    echo Creando entorno virtual...
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: No se pudo crear el entorno virtual
        pause
        exit /b 1
    )
    echo [✓] Entorno virtual creado
) else (
    echo [✓] Entorno virtual ya existe
)

echo.
echo ============================================================================
echo PASO 3: Activar entorno virtual
echo ============================================================================
echo.

call venv\Scripts\activate.bat

if errorlevel 1 (
    echo ERROR: No se pudo activar el entorno virtual
    pause
    exit /b 1
)

echo [✓] Entorno virtual activado

echo.
echo ============================================================================
echo PASO 4: Instalar dependencias optimizadas para Windows
echo ============================================================================
echo.

echo Instalando dependencias (esto puede tomar 5-10 minutos)...
echo.

pip install -r requirements_windows_optimized.txt --no-cache-dir

if errorlevel 1 (
    echo ERROR: No se pudo instalar las dependencias
    echo.
    echo Intentando instalar dependencias individuales...
    echo.
    
    REM Instalar dependencias críticas primero
    echo Instalando pandas...
    pip install pandas --no-cache-dir
    
    echo Instalando numpy...
    pip install numpy --no-cache-dir
    
    echo Instalando fastapi y uvicorn...
    pip install fastapi uvicorn --no-cache-dir
    
    echo Instalando MetaTrader5...
    pip install MetaTrader5 --no-cache-dir
    
    echo Instalando pandas-ta...
    pip install pandas-ta --no-cache-dir
    
    echo Instalando dependencias de Telegram...
    pip install python-telegram-bot --no-cache-dir
    
    echo Instalando dependencias de Gmail...
    pip install google-auth-oauthlib google-api-python-client --no-cache-dir
    
    echo Instalando dependencias de Excel...
    pip install openpyxl --no-cache-dir
    
    echo Instalando dependencias adicionales...
    pip install websockets aiofiles requests python-dotenv sqlalchemy --no-cache-dir
)

echo.
echo [✓] Dependencias instaladas exitosamente

echo.
echo ============================================================================
echo PASO 5: Verificar instalación
echo ============================================================================
echo.

echo Verificando módulos críticos...
echo.

python -c "import pandas; print('[✓] pandas:', pandas.__version__)" 2>nul || echo "[✗] pandas NO instalado"
python -c "import numpy; print('[✓] numpy:', numpy.__version__)" 2>nul || echo "[✗] numpy NO instalado"
python -c "import fastapi; print('[✓] fastapi:', fastapi.__version__)" 2>nul || echo "[✗] fastapi NO instalado"
python -c "import uvicorn; print('[✓] uvicorn:', uvicorn.__version__)" 2>nul || echo "[✗] uvicorn NO instalado"
python -c "import MetaTrader5; print('[✓] MetaTrader5 disponible')" 2>nul || echo "[✗] MetaTrader5 NO instalado"
python -c "import pandas_ta; print('[✓] pandas-ta:', pandas_ta.__version__)" 2>nul || echo "[✗] pandas-ta NO instalado"

echo.
echo ============================================================================
echo PASO 6: Ejecutar diagnóstico
echo ============================================================================
echo.

if exist "scripts\diagnostics.py" (
    echo Ejecutando diagnóstico del sistema...
    python scripts\diagnostics.py
) else (
    echo [!] Script de diagnóstico no encontrado en scripts\diagnostics.py
)

echo.
echo ============================================================================
echo INSTALACIÓN COMPLETADA
echo ============================================================================
echo.
echo Próximos pasos:
echo 1. Configura el archivo .env con tus credenciales
echo 2. Ejecuta: python run_system.bat
echo 3. Accede al dashboard en http://localhost:8000
echo.
echo Para más información, consulta SISETRWEB_WINDOWS_INSTALLATION_GUIDE.md
echo.

pause
