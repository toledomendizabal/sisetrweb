# Solución DEFINITIVA: Python 3.14 + Numba + Pandas-ta

## 🔴 Error Reportado

```
RuntimeError: Cannot install on Python version 3.14.4; 
only versions >=3.10,<3.14 are supported.
ERROR: Failed to build 'numba' when getting requirements to build wheel
ModuleNotFoundError: No module named 'apscheduler'
```

## 🔍 Causa Raíz

Tu sistema está ejecutando **Python 3.14.4**, que es una versión de desarrollo. El problema es que:

1. **Numba** (dependencia de pandas-ta) **no soporta Python 3.14** - solo soporta hasta Python 3.13
2. **pandas-ta** depende de numba, por lo que tampoco funciona
3. Falta **APScheduler**, que es crítico para el bot

---

## ✅ Soluciones

### Solución 1: Usar Python 3.11 o 3.13 (RECOMENDADO)

La forma más sencilla es usar una versión estable de Python que sea soportada por todas las librerías.

**Pasos:**

1. **Descargar Python 3.11 o 3.13:**
   - Visita https://www.python.org/downloads/
   - Descarga Python 3.11.x o Python 3.13.x (NO 3.14)
   - Durante la instalación, marca "Add Python to PATH"

2. **Verificar instalación:**
   ```bash
   python --version
   # Debe mostrar: Python 3.11.x o Python 3.13.x
   ```

3. **Limpiar e instalar nuevamente:**
   ```bash
   # Eliminar entorno virtual anterior
   rmdir /s /q venv
   
   # Crear nuevo entorno virtual
   python -m venv venv
   
   # Activar
   .\venv\Scripts\activate
   
   # Instalar dependencias
   pip install -r requirements_final.txt --no-cache-dir
   ```

---

### Solución 2: Mantener Python 3.14 + Usar Módulo Python Puro

Si prefieres mantener Python 3.14, usa el módulo de análisis técnico en Python puro que **no depende de numba ni pandas-ta**.

**Pasos:**

1. **Instalar dependencias FINALES:**
   ```bash
   # Limpiar entorno anterior
   rmdir /s /q venv
   
   # Crear nuevo entorno
   python -m venv venv
   
   # Activar
   .\venv\Scripts\activate
   
   # Instalar dependencias (sin pandas-ta ni numba)
   pip install -r requirements_final.txt --no-cache-dir
   ```

2. **Copiar módulo de análisis técnico Python puro:**
   ```bash
   copy src\engines\technical_analysis_pure_python.py src\engines\technical_analysis.py
   ```

3. **Iniciar el bot:**
   ```bash
   python run_system.bat
   ```

---

### Solución 3: Usar el Script de Instalación DEFINITIVO

Ejecuta el script que automatiza todo:

```bash
.\install_final.bat
```

Este script:
- ✅ Limpia la instalación anterior
- ✅ Actualiza pip y setuptools
- ✅ Instala dependencias FINALES (sin numba)
- ✅ Copia el módulo Python puro
- ✅ Verifica la instalación
- ✅ Ejecuta el diagnóstico

---

## 📊 Comparativa de Soluciones

| Solución | Facilidad | Compatibilidad | Rendimiento | Recomendación |
|----------|-----------|----------------|-------------|---------------|
| **1. Python 3.11/3.13** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 🏆 MEJOR |
| **2. Python 3.14 + Puro** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ✅ Válida |
| **3. Script install_final.bat** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ✅ Automática |

---

## ⚡ Solución Rápida (5 minutos)

### Si Cambias a Python 3.11/3.13:

```bash
# 1. Descargar Python 3.11 desde https://www.python.org/downloads/
# 2. Instalar (marca "Add Python to PATH")
# 3. Ejecutar en PowerShell:

rmdir /s /q venv
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements_final.txt --no-cache-dir
python run_system.bat
```

### Si Mantienes Python 3.14:

```bash
# 1. Ejecutar el script automático
.\install_final.bat

# 2. O manualmente:
rmdir /s /q venv
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements_final.txt --no-cache-dir
copy src\engines\technical_analysis_pure_python.py src\engines\technical_analysis.py
python run_system.bat
```

---

## 📋 Archivos Necesarios

He creado los siguientes archivos para resolver este problema:

| Archivo | Propósito |
|---------|-----------|
| **requirements_final.txt** | Dependencias sin numba/pandas-ta (compatible con Python 3.14) |
| **technical_analysis_pure_python.py** | Indicadores técnicos en Python puro (sin compilación) |
| **install_final.bat** | Script de instalación automática |

---

## 🔧 Diferencias Entre Módulos de Análisis Técnico

| Módulo | Dependencias | Python 3.14 | Rendimiento | Indicadores |
|--------|-------------|-----------|-------------|------------|
| **technical_analysis.py** (original) | talib | ❌ No | ⭐⭐⭐⭐⭐ | 8 |
| **technical_analysis_alternative.py** | pandas-ta + numba | ❌ No | ⭐⭐⭐⭐ | 8 |
| **technical_analysis_pure_python.py** | numpy + pandas | ✅ Sí | ⭐⭐⭐⭐ | 8 |

Todos implementan los **mismos 8 indicadores técnicos**:
- RSI (Índice de Fuerza Relativa)
- MACD (Moving Average Convergence Divergence)
- Bandas de Bollinger
- ATR (Rango Verdadero Promedio)
- Estocástico
- EMA (Media Móvil Exponencial)
- SMA (Media Móvil Simple)
- ADX (Índice Direccional Promedio)

---

## ✅ Verificación Post-Instalación

Después de instalar, verifica que todo funciona:

```bash
# 1. Activar entorno virtual
.\venv\Scripts\activate

# 2. Verificar módulos críticos
python -c "
import pandas as pd
import numpy as np
import fastapi
import uvicorn
import MetaTrader5 as mt5
import apscheduler

print('✅ pandas:', pd.__version__)
print('✅ numpy:', np.__version__)
print('✅ fastapi:', fastapi.__version__)
print('✅ uvicorn:', uvicorn.__version__)
print('✅ MetaTrader5: disponible')
print('✅ APScheduler: disponible')
print()
print('🎉 Todos los módulos se instalaron correctamente!')
"

# 3. Ejecutar diagnóstico
python scripts/diagnostics.py

# 4. Iniciar el bot
python run_system.bat
```

---

## 📞 Si Aún Tienes Problemas

1. **Verifica tu versión de Python:**
   ```bash
   python --version
   ```

2. **Limpia la caché de pip:**
   ```bash
   pip cache purge
   ```

3. **Reinstala desde cero:**
   ```bash
   rmdir /s /q venv
   python -m venv venv
   .\venv\Scripts\activate
   pip install --upgrade pip setuptools wheel
   pip install -r requirements_final.txt --no-cache-dir
   ```

4. **Abre un issue en GitHub:**
   https://github.com/toledomendizabal/sisetrweb/issues

---

## 🎯 Recomendación Final

**Usa Python 3.11 o 3.13** porque:
- ✅ Máxima compatibilidad con todas las librerías
- ✅ Mejor rendimiento
- ✅ Mejor soporte comunitario
- ✅ Instalación más sencilla

Python 3.14 es una versión de desarrollo y aún no tiene soporte completo en muchas librerías científicas.

---

**Última actualización**: Mayo 2026  
**Versión**: 1.0  
**Autor**: SISETRWEB Development Team
