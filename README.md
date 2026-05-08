# SISETRWEB Bot de Trading Autogestionado

Este proyecto implementa un bot de trading autogestionado para Forex, Oro e Índices, con análisis técnico en tiempo real, generación de señales, gestión de riesgo, backtesting, y un dashboard web interactivo. El sistema está diseñado para operar en un ambiente Windows y utiliza Python como lenguaje principal.

## Estructura del Proyecto

```
sisetrweb_bot/
├── src/
│   ├── core/                  # Módulos principales: configuración, modelos de datos, utilidades
│   ├── engines/               # Motores de análisis técnico, señales, monitoreo
│   ├── managers/              # Gestión de Excel, Telegram, Email, Riesgo
│   ├── api/                   # Lógica del backend FastAPI y WebSockets
│   ├── utils/                 # Funciones de utilidad, helpers
│   └── main.py                # Punto de entrada principal del bot
├── config/                    # Archivos de configuración (JSON, YAML, etc.)
├── data/                      # Archivos de datos (Excel para señales, backtesting, etc.)
├── logs/                      # Archivos de registro del sistema
├── scripts/                   # Scripts de inicio (.bat) y utilidades de ejecución
├── .env                       # Variables de entorno (API keys, tokens)
├── requirements.txt           # Dependencias de Python
└── README.md                  # Documentación del proyecto
```

## Instalación (Guía Rápida)

1.  **Clonar el repositorio:**
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd sisetrweb_bot
    ```
2.  **Crear y activar un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configurar variables de entorno:**
    Crear un archivo `.env` en la raíz del proyecto y añadir las variables necesarias (ej. `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`, `TWELVEDATA_API_KEY`, `GMAIL_CLIENT_SECRET_PATH`).

5.  **Ejecutar el bot:**
    ```bash
    python src/main.py
    ```
    O usar el script `run_system.bat` para iniciar todos los componentes.

## Requisitos del Sistema

-   Sistema Operativo: Windows 10/11
-   Python: 3.9 o superior (se recomienda 3.11)
-   MetaTrader 5 (para la conexión de datos principal)

## Contacto

Para soporte o consultas, contactar a [tu_correo@ejemplo.com].
