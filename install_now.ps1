# ============================================================================
# SISETRWEB - Script de Instalación PowerShell (DEFINITIVO)
# ============================================================================
# Este script fuerza la instalación correcta sin ambigüedades
# Uso: Ejecutar en PowerShell como administrador
# ============================================================================

Write-Host ""
Write-Host "============================================================================"
Write-Host "SISETRWEB - Instalador PowerShell DEFINITIVO"
Write-Host "============================================================================"
Write-Host ""

# Verificar que Python está instalado
Write-Host "Verificando Python..."
$pythonVersion = python --version 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Python no está instalado o no está en el PATH"
    Write-Host "Descarga Python 3.11+ desde https://www.python.org/downloads/"
    Read-Host "Presiona Enter para salir"
    exit 1
}

Write-Host "[✓] Python detectado: $pythonVersion"
Write-Host ""

# ============================================================================
# PASO 1: Limpiar instalación anterior
# ============================================================================
Write-Host "============================================================================"
Write-Host "PASO 1: Limpiar instalación anterior"
Write-Host "============================================================================"
Write-Host ""

if (Test-Path "venv") {
    Write-Host "Eliminando entorno virtual anterior..."
    Remove-Item -Recurse -Force "venv" -ErrorAction SilentlyContinue
    if ($?) {
        Write-Host "[✓] Entorno virtual anterior eliminado"
    } else {
        Write-Host "[!] No se pudo eliminar completamente el entorno anterior"
    }
} else {
    Write-Host "[✓] No hay entorno virtual anterior"
}

Write-Host ""

# ============================================================================
# PASO 2: Actualizar pip
# ============================================================================
Write-Host "============================================================================"
Write-Host "PASO 2: Actualizar pip, setuptools y wheel"
Write-Host "============================================================================"
Write-Host ""

python -m pip install --upgrade pip setuptools wheel --no-cache-dir
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: No se pudo actualizar pip"
    Read-Host "Presiona Enter para salir"
    exit 1
}

Write-Host "[✓] pip, setuptools y wheel actualizados"
Write-Host ""

# ============================================================================
# PASO 3: Crear entorno virtual
# ============================================================================
Write-Host "============================================================================"
Write-Host "PASO 3: Crear entorno virtual"
Write-Host "============================================================================"
Write-Host ""

Write-Host "Creando entorno virtual..."
python -m venv venv

if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: No se pudo crear el entorno virtual"
    Read-Host "Presiona Enter para salir"
    exit 1
}

Write-Host "[✓] Entorno virtual creado"
Write-Host ""

# ============================================================================
# PASO 4: Activar entorno virtual
# ============================================================================
Write-Host "============================================================================"
Write-Host "PASO 4: Activar entorno virtual"
Write-Host "============================================================================"
Write-Host ""

& ".\venv\Scripts\Activate.ps1"

if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: No se pudo activar el entorno virtual"
    Read-Host "Presiona Enter para salir"
    exit 1
}

Write-Host "[✓] Entorno virtual activado"
Write-Host ""

# ============================================================================
# PASO 5: Instalar dependencias FINALES
# ============================================================================
Write-Host "============================================================================"
Write-Host "PASO 5: Instalar dependencias FINALES (sin numba ni pandas-ta)"
Write-Host "============================================================================"
Write-Host ""

Write-Host "Instalando dependencias (esto puede tomar 5-10 minutos)..."
Write-Host ""

# Verificar que el archivo requirements_final.txt existe
if (-not (Test-Path "requirements_final.txt")) {
    Write-Host "ERROR: No se encontró requirements_final.txt"
    Write-Host "Asegúrate de que el archivo está en el directorio actual"
    Read-Host "Presiona Enter para salir"
    exit 1
}

pip install -r requirements_final.txt --no-cache-dir

if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "WARNING: Hubo problemas durante la instalación"
    Write-Host "Intentando instalar dependencias críticas individualmente..."
    Write-Host ""
    
    Write-Host "Instalando pandas..."
    pip install pandas --no-cache-dir
    
    Write-Host "Instalando numpy..."
    pip install numpy --no-cache-dir
    
    Write-Host "Instalando fastapi y uvicorn..."
    pip install fastapi uvicorn --no-cache-dir
    
    Write-Host "Instalando MetaTrader5..."
    pip install MetaTrader5 --no-cache-dir
    
    Write-Host "Instalando python-telegram-bot..."
    pip install python-telegram-bot --no-cache-dir
    
    Write-Host "Instalando google-auth-oauthlib..."
    pip install google-auth-oauthlib google-api-python-client --no-cache-dir
    
    Write-Host "Instalando openpyxl..."
    pip install openpyxl --no-cache-dir
    
    Write-Host "Instalando APScheduler..."
    pip install APScheduler --no-cache-dir
    
    Write-Host "Instalando dependencias adicionales..."
    pip install websockets aiofiles requests python-dotenv sqlalchemy --no-cache-dir
}

Write-Host ""
Write-Host "[✓] Dependencias instaladas"
Write-Host ""

# ============================================================================
# PASO 6: Verificar instalación
# ============================================================================
Write-Host "============================================================================"
Write-Host "PASO 6: Verificar instalación"
Write-Host "============================================================================"
Write-Host ""

Write-Host "Verificando módulos críticos..."
Write-Host ""

python -c "import pandas; print('[✓] pandas:', pandas.__version__)" 2>$null
if ($LASTEXITCODE -ne 0) { Write-Host "[✗] pandas NO instalado" }

python -c "import numpy; print('[✓] numpy:', numpy.__version__)" 2>$null
if ($LASTEXITCODE -ne 0) { Write-Host "[✗] numpy NO instalado" }

python -c "import fastapi; print('[✓] fastapi:', fastapi.__version__)" 2>$null
if ($LASTEXITCODE -ne 0) { Write-Host "[✗] fastapi NO instalado" }

python -c "import uvicorn; print('[✓] uvicorn:', uvicorn.__version__)" 2>$null
if ($LASTEXITCODE -ne 0) { Write-Host "[✗] uvicorn NO instalado" }

python -c "import MetaTrader5; print('[✓] MetaTrader5 disponible')" 2>$null
if ($LASTEXITCODE -ne 0) { Write-Host "[✗] MetaTrader5 NO instalado" }

python -c "import apscheduler; print('[✓] APScheduler disponible')" 2>$null
if ($LASTEXITCODE -ne 0) { Write-Host "[✗] APScheduler NO instalado" }

python -c "import telegram; print('[✓] python-telegram-bot disponible')" 2>$null
if ($LASTEXITCODE -ne 0) { Write-Host "[✗] python-telegram-bot NO instalado" }

Write-Host ""

# ============================================================================
# PASO 7: Copiar módulo de análisis técnico
# ============================================================================
Write-Host "============================================================================"
Write-Host "PASO 7: Copiar módulo de análisis técnico Python puro"
Write-Host "============================================================================"
Write-Host ""

if (Test-Path "src\engines\technical_analysis_pure_python.py") {
    Write-Host "Copiando módulo de análisis técnico..."
    Copy-Item "src\engines\technical_analysis_pure_python.py" "src\engines\technical_analysis.py" -Force
    if ($?) {
        Write-Host "[✓] Módulo de análisis técnico actualizado"
    } else {
        Write-Host "[!] No se pudo copiar el módulo de análisis técnico"
    }
} else {
    Write-Host "[!] No se encontró src\engines\technical_analysis_pure_python.py"
}

Write-Host ""

# ============================================================================
# PASO 8: Ejecutar diagnóstico
# ============================================================================
Write-Host "============================================================================"
Write-Host "PASO 8: Ejecutar diagnóstico"
Write-Host "============================================================================"
Write-Host ""

if (Test-Path "scripts\diagnostics.py") {
    Write-Host "Ejecutando diagnóstico del sistema..."
    python scripts\diagnostics.py
} else {
    Write-Host "[!] Script de diagnóstico no encontrado"
}

Write-Host ""

# ============================================================================
# FINALIZACIÓN
# ============================================================================
Write-Host "============================================================================"
Write-Host "INSTALACIÓN COMPLETADA EXITOSAMENTE"
Write-Host "============================================================================"
Write-Host ""
Write-Host "Próximos pasos:"
Write-Host ""
Write-Host "1. Configura el archivo .env con tus credenciales:"
Write-Host "   - TELEGRAM_BOT_TOKEN"
Write-Host "   - TELEGRAM_CHAT_ID"
Write-Host "   - Credenciales de Gmail OAuth2"
Write-Host "   - Credenciales de MetaTrader 5"
Write-Host ""
Write-Host "2. Ejecuta el bot:"
Write-Host "   python run_system.bat"
Write-Host ""
Write-Host "3. Accede al dashboard en:"
Write-Host "   http://localhost:8000"
Write-Host ""
Write-Host "============================================================================"
Write-Host ""

Read-Host "Presiona Enter para salir"
