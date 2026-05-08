# 📦 Paquete de Instalación SISETRWEB - Python 3.14 Compatible

## ⚠️ IMPORTANTE

Este paquete contiene todos los archivos necesarios para instalar SISETRWEB correctamente en Windows con Python 3.14.

---

## 📋 Archivos Incluidos

1. **INSTRUCCIONES_URGENTES.md** - Guía rápida (LEE ESTO PRIMERO)
2. **PYTHON_314_NUMBA_FIX.md** - Documentación técnica completa
3. **requirements_final.txt** - Dependencias correctas (SIN numba)
4. **technical_analysis_pure_python.py** - Módulo de análisis técnico
5. **install_now.ps1** - Script PowerShell automático (RECOMENDADO)
6. **install_final.bat** - Script Batch automático (ALTERNATIVA)

---

## 🚀 INSTALACIÓN RÁPIDA (3 PASOS)

### Paso 1: Copiar Archivos a tu Carpeta SISETRWEB

Copia todos los archivos de este paquete a tu carpeta `C:\xampp\htdocs\sisetrweb\`:

```
C:\xampp\htdocs\sisetrweb\
├── requirements_final.txt          ← Copiar aquí
├── technical_analysis_pure_python.py  ← Copiar en src\engines\
├── install_now.ps1                 ← Copiar aquí
├── install_final.bat               ← Copiar aquí
├── INSTRUCCIONES_URGENTES.md       ← Copiar aquí
└── ... (otros archivos existentes)
```

**Estructura correcta después de copiar:**
```
C:\xampp\htdocs\sisetrweb\
├── requirements_final.txt
├── install_now.ps1
├── install_final.bat
├── src\
│   └── engines\
│       └── technical_analysis_pure_python.py
└── ... (otros archivos)
```

### Paso 2: Ejecutar el Script de Instalación

Abre PowerShell en tu carpeta SISETRWEB y ejecuta:

```powershell
cd C:\xampp\htdocs\sisetrweb
.\install_now.ps1
```

**O si prefieres Batch:**

```cmd
cd C:\xampp\htdocs\sisetrweb
.\install_final.bat
```

### Paso 3: Esperar a que Termine

El script hará TODO automáticamente:
- ✅ Limpia entorno anterior
- ✅ Crea nuevo entorno virtual
- ✅ Instala dependencias correctas
- ✅ Copia módulo de análisis técnico
- ✅ Verifica instalación
- ✅ Ejecuta diagnóstico

**Tiempo estimado: 10-15 minutos**

---

## ✅ Verificación

Después de que termine el script, verifica que todo funciona:

```bash
# Activar entorno (si no está ya activado)
.\venv\Scripts\activate

# Verificar módulos
python -c "
import pandas
import fastapi
import uvicorn
import apscheduler
print('✅ Todo instalado correctamente!')
"

# Iniciar el bot
python run_system.bat
```

---

## 📍 Ubicación de Archivos

Asegúrate de copiar los archivos en las ubicaciones correctas:

| Archivo | Ubicación |
|---------|-----------|
| requirements_final.txt | `C:\xampp\htdocs\sisetrweb\` |
| technical_analysis_pure_python.py | `C:\xampp\htdocs\sisetrweb\src\engines\` |
| install_now.ps1 | `C:\xampp\htdocs\sisetrweb\` |
| install_final.bat | `C:\xampp\htdocs\sisetrweb\` |

---

## 🆘 Si Algo Falla

1. **Lee INSTRUCCIONES_URGENTES.md**
2. **Lee PYTHON_314_NUMBA_FIX.md**
3. **Limpia y comienza de nuevo:**
   ```bash
   rmdir /s /q venv
   pip cache purge
   .\install_now.ps1
   ```

---

## 📞 Soporte

Si aún tienes problemas:
1. Abre un issue en GitHub: https://github.com/toledomendizabal/sisetrweb/issues
2. Incluye el archivo de error/log
3. Describe qué paso falló

---

**Última actualización**: Mayo 2026
**Versión**: 1.0
**Compatible con**: Python 3.11, 3.12, 3.13, 3.14+
