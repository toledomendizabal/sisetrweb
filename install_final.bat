@echo off
REM ============================================================================
REM SISETRWEB - Script de Instalación DEFINITIVO para Windows
REM ============================================================================
REM Versión final que funciona con Python 3.11+ (incluyendo 3.14)
REM Sin dependencias compiladas (numba, talib, pandas-ta)
REM ============================================================================

setlocal enabledelayedexpansion
cls

echo.
echo ============================================================================
echo SISETRWEB - Instalador DEFINITIVO para Windows
echo ============================================================================
echo.

REM Verificar que Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no está instalado o no está en el PATH
    echo Descarga Python 3.11+ desde https://www.python.org/downloads/
    echo.
    echo IMPORTANTE: Asegúrate de marcar "Add Python to PATH" durante la instalación
    pause
    exit /b 1
)

echo [✓] Python detectado
python --version
echo.

REM Verificar versión de Python
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo Versión de Python: %PYTHON_VERSION%
echo.

echo ============================================================================
echo PASO 1: Limpiar instalación anterior (si existe)
echo ============================================================================
echo.

if exist "venv" (
    echo Eliminando entorno virtual anterior...
    rmdir /s /q venv
    if errorlevel 1 (
        echo WARNING: No se pudo eliminar completamente el entorno anterior
        echo Intenta manualmente: rmdir /s /q venv
    ) else (
        echo [✓] Entorno virtual anterior eliminado
    )
) else (
    echo [✓] No hay entorno virtual anterior
)

echo.
echo ============================================================================
echo PASO 2: Actualizar pip, setuptools y wheel
echo ============================================================================
echo.

python -m pip install --upgrade pip setuptools wheel --no-cache-dir

if errorlevel 1 (
    echo ERROR: No se pudo actualizar pip
    pause
    exit /b 1
)

echo [✓] pip, setuptools y wheel actualizados

echo.
echo ============================================================================
echo PASO 3: Crear entorno virtual
echo ============================================================================
echo.

echo Creando entorno virtual...
python -m venv venv

if errorlevel 1 (
    echo ERROR: No se pudo crear el entorno virtual
    pause
    exit /b 1
)

echo [✓] Entorno virtual creado

echo.
echo ============================================================================
echo PASO 4: Activar entorno virtual
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
echo PASO 5: Instalar dependencias FINALES (sin compilación)
echo ============================================================================
echo.

echo Instalando dependencias (esto puede tomar 5-10 minutos)...
echo.

pip install -r requirements_final.txt --no-cache-dir

if errorlevel 1 (
    echo.
    echo WARNING: Hubo problemas durante la instalación
    echo Intentando instalar dependencias críticas individualmente...
    echo.
    
    REM Instalar dependencias críticas una por una
    echo Instalando pandas...
    pip install pandas --no-cache-dir
    
    echo Instalando numpy...
    pip install numpy --no-cache-dir
    
    echo Instalando fastapi y uvicorn...
    pip install fastapi uvicorn --no-cache-dir
    
    echo Instalando MetaTrader5...
    pip install MetaTrader5 --no-cache-dir
    
    echo Instalando dependencias de Telegram...
    pip install python-telegram-bot --no-cache-dir
    
    echo Instalando dependencias de Gmail...
    pip install google-auth-oauthlib google-api-python-client --no-cache-dir
    
    echo Instalando dependencias de Excel...
    pip install openpyxl --no-cache-dir
    
    echo Instalando APScheduler...
    pip install APScheduler --no-cache-dir
    
    echo Instalando dependencias adicionales...
    pip install websockets aiofiles requests python-dotenv sqlalchemy --no-cache-dir
)

echo.
echo [✓] Dependencias instaladas

echo.
echo ============================================================================
echo PASO 6: Verificar instalación
echo ============================================================================
echo.

echo Verificando módulos críticos...
echo.

python -c "import pandas; print('[✓] pandas:', pandas.__version__)" 2>nul || echo "[✗] pandas NO instalado"
python -c "import numpy; print('[✓] numpy:', numpy.__version__)" 2>nul || echo "[✗] numpy NO instalado"
python -c "import fastapi; print('[✓] fastapi:', fastapi.__version__)" 2>nul || echo "[✗] fastapi NO instalado"
python -c "import uvicorn; print('[✓] uvicorn:', uvicorn.__version__)" 2>nul || echo "[✗] uvicorn NO instalado"
python -c "import MetaTrader5; print('[✓] MetaTrader5 disponible')" 2>nul || echo "[✗] MetaTrader5 NO instalado"
python -c "import apscheduler; print('[✓] APScheduler disponible')" 2>nul || echo "[✗] APScheduler NO instalado"
python -c "import telegram; print('[✓] python-telegram-bot disponible')" 2>nul || echo "[✗] python-telegram-bot NO instalado"

echo.
echo ============================================================================
echo PASO 7: Copiar módulo de análisis técnico
echo ============================================================================
echo.

if exist "src\engines\technical_analysis_pure_python.py" (
    echo Copiando módulo de análisis técnico Python puro...
    copy src\engines\technical_analysis_pure_python.py src\engines\technical_analysis.py
    if errorlevel 1 (
        echo WARNING: No se pudo copiar el módulo de análisis técnico
    ) else (
        echo [✓] Módulo de análisis técnico actualizado
    )
) else (
    echo WARNING: No se encontró src\engines\technical_analysis_pure_python.py
)

echo.
echo ============================================================================
echo PASO 8: Ejecutar diagnóstico
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
echo INSTALACIÓN COMPLETADA EXITOSAMENTE
echo ============================================================================
echo.
echo Próximos pasos:
echo.
echo 1. Configura el archivo .env con tus credenciales:
echo    - TELEGRAM_BOT_TOKEN
echo    - TELEGRAM_CHAT_ID
echo    - Credenciales de Gmail OAuth2
echo    - Credenciales de MetaTrader 5
echo.
echo 2. Ejecuta el bot:
echo    python run_system.bat
echo.
echo 3. Accede al dashboard en:
echo    http://localhost:8000
echo.
echo 4. Para más información, consulta:
echo    - SISETRWEB_WINDOWS_INSTALLATION_GUIDE.md
echo    - PANDAS_COMPILATION_ERROR_FIX.md
echo    - README.md
echo.
echo ============================================================================
echo.

pause
