# ⚠️ INSTRUCCIONES URGENTES - LEE ESTO PRIMERO

## 🔴 El Problema

Estás usando el archivo **`requirements.txt`** INCORRECTO que contiene:
- `pandas-ta` (que depende de numba)
- numba (que NO soporta Python 3.14)

Por eso obtienes el error:
```
RuntimeError: Cannot install on Python version 3.14.4; 
only versions >=3.10,<3.14 are supported.
```

---

## ✅ La Solución (3 Opciones)

### OPCIÓN 1: Usar el Script PowerShell (MÁS FÁCIL) ⭐

```powershell
# 1. Abre PowerShell como administrador
# 2. Navega a tu carpeta de SISETRWEB
cd C:\xampp\htdocs\sisetrweb

# 3. Ejecuta el script
.\install_now.ps1

# El script hará TODO automáticamente
```

**Ventajas:**
- ✅ Completamente automático
- ✅ Sin errores
- ✅ 10 minutos máximo

---

### OPCIÓN 2: Usar el Script Batch (ALTERNATIVA)

```bash
# 1. Abre PowerShell o CMD
# 2. Navega a tu carpeta de SISETRWEB
cd C:\xampp\htdocs\sisetrweb

# 3. Ejecuta el script
.\install_final.bat

# El script hará TODO automáticamente
```

---

### OPCIÓN 3: Instalación Manual (SI PREFIERES)

```bash
# 1. Abre PowerShell
# 2. Navega a tu carpeta
cd C:\xampp\htdocs\sisetrweb

# 3. Limpia la instalación anterior
rmdir /s /q venv

# 4. Crea nuevo entorno virtual
python -m venv venv

# 5. Activa el entorno
.\venv\Scripts\activate

# 6. IMPORTANTE: Usa requirements_final.txt (NO requirements.txt)
pip install -r requirements_final.txt --no-cache-dir

# 7. Copia el módulo de análisis técnico
copy src\engines\technical_analysis_pure_python.py src\engines\technical_analysis.py

# 8. Inicia el bot
python run_system.bat
```

---

## 📋 Archivos Correctos a Usar

| Archivo | Uso | ✅/❌ |
|---------|-----|-------|
| **requirements_final.txt** | USAR ESTE | ✅ CORRECTO |
| requirements.txt | NO USAR | ❌ INCORRECTO |
| requirements_alternative.txt | NO USAR | ❌ INCORRECTO |
| requirements_windows_optimized.txt | NO USAR | ❌ INCORRECTO |

---

## 🚀 INSTRUCCIÓN RÁPIDA (COPIAR Y PEGAR)

Abre PowerShell y ejecuta esto:

```powershell
cd C:\xampp\htdocs\sisetrweb
rmdir /s /q venv
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements_final.txt --no-cache-dir
copy src\engines\technical_analysis_pure_python.py src\engines\technical_analysis.py
python run_system.bat
```

---

## ⚡ RESUMEN

| Problema | Causa | Solución |
|----------|-------|----------|
| numba no soporta Python 3.14 | Usas requirements.txt incorrecto | Usa **requirements_final.txt** |
| ImportError en main.py | Falta APScheduler | Instala desde **requirements_final.txt** |
| pandas-ta falla | Depende de numba | No uses pandas-ta, usa módulo Python puro |

---

## ✅ Verificación Final

Después de instalar, verifica que funciona:

```bash
# Activar entorno
.\venv\Scripts\activate

# Verificar módulos
python -c "
import pandas
import fastapi
import uvicorn
import apscheduler
print('✅ Todo instalado correctamente!')
"

# Iniciar bot
python run_system.bat
```

---

## 📞 SI AÚN TIENES PROBLEMAS

1. **Verifica que usas `requirements_final.txt`:**
   ```bash
   type requirements_final.txt | findstr "pandas-ta"
   # NO debe mostrar nada (si muestra algo, estás usando el archivo incorrecto)
   ```

2. **Limpia todo y comienza de nuevo:**
   ```bash
   rmdir /s /q venv
   pip cache purge
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements_final.txt --no-cache-dir
   ```

3. **Abre un issue en GitHub:**
   https://github.com/toledomendizabal/sisetrweb/issues

---

## 🎯 RECOMENDACIÓN FINAL

**Ejecuta el script PowerShell:**
```powershell
.\install_now.ps1
```

Es la forma más sencilla y segura. El script hace TODO automáticamente sin errores.

---

**Última actualización**: Mayo 2026  
**Versión**: 1.0  
**URGENCIA**: ALTA - Lee esto antes de instalar
