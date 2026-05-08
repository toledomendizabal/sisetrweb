# Guía de Instalación - SISETRWEB

Esta guía proporciona instrucciones paso a paso para instalar y configurar SISETRWEB en un ambiente Windows.

## Requisitos del Sistema

| Componente | Requisito Mínimo | Versión Recomendada |
| :--- | :--- | :--- |
| **Sistema Operativo** | Windows 10 | Windows 11 |
| **Python** | 3.9.x | 3.11.x |
| **MetaTrader 5** | Terminal Instalada | Terminal con Login Activo |
| **Excel** | Microsoft Excel | Office 365 / 2021 |
| **RAM** | 4 GB | 8 GB o superior |
| **Espacio en Disco** | 500 MB | 1 GB |

## Verificación de Versiones de Python

Antes de instalar, verifica que tienes Python 3.9 o superior:

```bash
python --version
```

Si obtienes un error, descarga Python desde [python.org](https://www.python.org/downloads/) e instálalo.

## Paso 1: Descargar el Proyecto

Descarga el archivo `sisetrweb_bot.zip` y descomprímelo en tu directorio preferido:

```
C:\Users\TuUsuario\Documentos\sisetrweb_bot\
```

## Paso 2: Configurar MetaTrader 5

1. Descarga e instala [MetaTrader 5](https://www.metatrader5.com/es/download)
2. Abre la terminal y inicia sesión con tu cuenta de broker
3. Verifica que puedas ver los símbolos (EURUSD, XAUUSD, etc.)

## Paso 3: Configurar Variables de Entorno

1. En la carpeta raíz del proyecto, renombra `.env.example` a `.env`
2. Edita el archivo `.env` y completa:

```env
TELEGRAM_BOT_TOKEN="Tu_Token_De_Telegram"
TELEGRAM_CHAT_ID="Tu_Chat_ID"
GMAIL_CLIENT_SECRET_PATH="client_secret.json"
GMAIL_SENDER_EMAIL="tu_correo@gmail.com"
GMAIL_RECIPIENT_EMAIL="tu_correo@gmail.com"
TWELVEDATA_API_KEY="Tu_API_Key_De_Twelve_Data"
```

### Obtener Telegram Bot Token

1. Abre Telegram y busca `@BotFather`
2. Envía `/newbot` y sigue las instrucciones
3. Copia el token proporcionado

### Obtener Gmail OAuth2 Credentials

1. Ve a [Google Cloud Console](https://console.cloud.google.com/)
2. Crea un nuevo proyecto
3. Habilita la API de Gmail
4. Crea credenciales OAuth2 (Desktop Application)
5. Descarga el archivo JSON como `client_secret.json`

## Paso 4: Instalación Automática (Recomendado)

Haz doble clic en el archivo `run_system.bat`. Este script:

- Crea un entorno virtual (`venv`)
- Instala todas las dependencias
- Inicia el bot automáticamente

## Paso 5: Instalación Manual (Alternativa)

Si prefieres instalar manualmente:

```bash
# Abrir PowerShell en la carpeta del proyecto
cd C:\Users\TuUsuario\Documentos\sisetrweb_bot

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
.\venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Iniciar el bot
python src/main.py
```

## Paso 6: Verificación de Instalación

Ejecuta el script de diagnóstico:

```bash
python scripts/diagnostics.py
```

Deberías ver:

```
--- Iniciando Diagnóstico de SISETRWEB ---
Python Version: 3.11.0
Verificando conexión con MetaTrader 5...
✅ Conexión con MT5 exitosa.
--- Diagnóstico Completado ---
```

## Paso 7: Acceso al Dashboard

Una vez iniciado el bot, accede al dashboard en:

```
http://localhost:8000
```

## Solución de Problemas

### Error: "Python no está instalado"

Descarga Python desde [python.org](https://www.python.org/downloads/) y asegúrate de marcar "Add Python to PATH" durante la instalación.

### Error: "MetaTrader 5 no encontrado"

Asegúrate de que MetaTrader 5 esté instalado y la terminal esté abierta con tu cuenta iniciada.

### Error: "Módulo no encontrado"

Verifica que el entorno virtual esté activado:

```bash
.\venv\Scripts\activate
```

Luego reinstala las dependencias:

```bash
pip install -r requirements.txt
```

### Error: "Token de Telegram inválido"

Verifica que hayas copiado correctamente el token en el archivo `.env`.

## Dependencias Principales

| Paquete | Versión | Uso |
| :--- | :--- | :--- |
| **FastAPI** | 0.136.0+ | Backend del dashboard |
| **Uvicorn** | 0.44.0+ | Servidor ASGI |
| **Pandas** | 3.0.2+ | Análisis de datos |
| **OpenPyXL** | 3.1.5+ | Gestión de Excel |
| **MetaTrader5** | Última | Conexión a MT5 |
| **python-telegram-bot** | Última | Integración Telegram |
| **google-api-python-client** | Última | Integración Gmail |
| **TA-Lib** | Última | Indicadores técnicos |
| **APScheduler** | Última | Tareas programadas |

## Configuración Inicial Recomendada

Después de la instalación, configura:

1. **Capital Base**: Ajusta en `config/settings.py` (default: $10,000)
2. **Riesgo por Operación**: Modifica `RIESGO_POR_OPERACION_PERCENT` (default: 0.3%)
3. **Activos**: Habilita/deshabilita en `ASSETS_CONFIG`
4. **Indicadores**: Personaliza parámetros según tu estrategia

## Próximos Pasos

1. Ejecuta el backtesting diario para validar la configuración
2. Revisa los logs en la carpeta `logs/`
3. Consulta la documentación completa en `README.md`

## Soporte

Para problemas o preguntas:

- Abre un issue en GitHub
- Consulta la documentación
- Contacta a los mantenedores

---

¡Instalación completada! Ahora puedes comenzar a usar SISETRWEB.
