# SISETRWEB - Bot de Trading Autogestionado Inteligente

[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub](https://img.shields.io/badge/GitHub-toledomendizabal%2Fsisetrweb-black)](https://github.com/toledomendizabal/sisetrweb)

**SISETRWEB** es una plataforma integral de trading autogestionada que automatiza la detección, validación, monitoreo y evaluación de señales de trading con alta probabilidad estadística y control estricto de riesgo. Diseñada para Forex, Oro e Índices con análisis técnico avanzado, generación inteligente de señales, gestión de riesgo automatizada y un dashboard web interactivo en tiempo real.

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

## 🎯 Características Principales

### Análisis Técnico Avanzado
- Indicadores multi-timeframe: EMA, RSI, MACD, Bollinger Bands, ATR, ADX, VWAP, Ichimoku
- Confirmaciones avanzadas: Patrones de velas y divergencias de RSI
- Análisis contextual: Filtros de sesión y correlaciones (DXY, VIX)

### Generación de Señales Inteligente
- Scoring automático (AAA, AA, A, Rechazada)
- Multi-confirmación en múltiples temporalidades
- Reglas de entrada estrictas con 12 condiciones técnicas

### Gestión de Riesgo Automatizada
- Cálculo dinámico de lotaje
- Stop Loss inteligente basado en ATR
- Take Profit escalonado (1:3, 1:6, 1:10)

### Integraciones Clave
- Telegram: Alertas instantáneas
- Gmail OAuth2: Reportes diarios de backtesting
- Excel Autogestionado: Registro y control de señales

## 📊 Activos Soportados

| Grupo | Instrumentos |
| :--- | :--- |
| **Forex Majors** | EURUSD, GBPUSD, USDJPY, USDCHF, USDCAD, AUDUSD, NZDUSD |
| **Oro** | XAUUSD |
| **Índices USA** | US30Cash, US100Cash, US500Cash |
| **Índices Europa** | GE40Cash |

## 🚀 Inicio Rápido

### Instalación Automática (Recomendado)

1. Descarga y descomprime el proyecto
2. Haz doble clic en `run_system.bat`
3. Completa la configuración en el archivo `.env`
4. Accede al dashboard en `http://localhost:8000`

### Instalación Manual

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno
.\venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el bot
python src/main.py
```

Para instrucciones detalladas, consulta [INSTALLATION.md](INSTALLATION.md).

## Requisitos del Sistema

-   Sistema Operativo: Windows 10/11
-   Python: 3.9 o superior (se recomienda 3.11)
-   MetaTrader 5 (para la conexión de datos principal)

## 📈 KPIs y Objetivos

| Métrica | Objetivo |
| :--- | :--- |
| **Win Rate** | > 55% |
| **Profit Factor** | > 1.5 |
| **Drawdown Máximo** | < 10% |
| **Latencia de Señales** | < 2 segundos |
| **Señales Falsas** | < 20% |
| **Disponibilidad** | 24/7 |

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Consulta [CONTRIBUTING.md](CONTRIBUTING.md) para más detalles.

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta [LICENSE](LICENSE) para más detalles.

## 📞 Contacto y Soporte

- **Issues**: [GitHub Issues](https://github.com/toledomendizabal/sisetrweb/issues)
- **Email**: support@sisetrweb.com
- **Documentación**: [INSTALLATION.md](INSTALLATION.md)

## ⚠️ Disclaimer

SISETRWEB es una herramienta de análisis técnico. El trading conlleva riesgo. Utiliza bajo tu propio riesgo y responsabilidad.

---

**Desarrollado por:** Manus AI | **Versión:** 1.0.0 | **Última Actualización:** Mayo 2026
