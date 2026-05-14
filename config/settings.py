
import os
from dotenv import load_dotenv

load_dotenv()

# --- Configuración General ---

CAPITAL_BASE = 10000  # Capital inicial para cálculo de lotaje
RIESGO_POR_OPERACION_PERCENT = 0.003  # 0.3% de riesgo por operación
MONITORING_INTERVAL_SECONDS = 10 # Intervalo de monitoreo de precios

# --- Activos Soportados ---

# Definición de activos con sus configuraciones específicas
# Se pueden habilitar/deshabilitar desde el dashboard
ASSETS_CONFIG = {
    "EURUSD": {"enabled": True, "group": "Forex", "timeframe_signal": ["1M", "3M", "5M"], "timeframe_trend": ["15M", "30M", "1H"]},
    "GBPUSD": {"enabled": True, "group": "Forex", "timeframe_signal": ["1M", "3M", "5M"], "timeframe_trend": ["15M", "30M", "1H"]},
    "USDJPY": {"enabled": True, "group": "Forex", "timeframe_signal": ["1M", "3M", "5M"], "timeframe_trend": ["15M", "30M", "1H"]},
    "USDCHF": {"enabled": True, "group": "Forex", "timeframe_signal": ["1M", "3M", "5M"], "timeframe_trend": ["15M", "30M", "1H"]},
    "USDCAD": {"enabled": True, "group": "Forex", "timeframe_signal": ["1M", "3M", "5M"], "timeframe_trend": ["15M", "30M", "1H"]},
    "AUDUSD": {"enabled": True, "group": "Forex", "timeframe_signal": ["1M", "3M", "5M"], "timeframe_trend": ["15M", "30M", "1H"]},
    "NZDUSD": {"enabled": True, "group": "Forex", "timeframe_signal": ["1M", "3M", "5M"], "timeframe_trend": ["15M", "30M", "1H"]},
    "GOLD": {"enabled": True, "group": "Oro", "timeframe_signal": ["1M", "3M", "5M"], "timeframe_trend": ["15M", "30M", "1H"]},
    "US30Cash": {"enabled": True, "group": "Indices", "timeframe_signal": ["1M", "3M", "5M"], "timeframe_trend": ["15M", "30M", "1H"]},
    "US100Cash": {"enabled": True, "group": "Indices", "timeframe_signal": ["1M", "3M", "5M"], "timeframe_trend": ["15M", "30M", "1H"]},
    "US500Cash": {"enabled": True, "group": "Indices", "timeframe_signal": ["1M", "3M", "5M"], "timeframe_trend": ["15M", "30M", "1H"]},
    "GE40Cash": {"enabled": True, "group": "Indices", "timeframe_signal": ["1M", "3M", "5M"], "timeframe_trend": ["15M", "30M", "1H"]},
}

# --- Configuración de Indicadores Técnicos ---

INDICATORS_CONFIG = {
    "EMA": {"periods": [9, 20, 50, 200]},
    "RSI": {"period": 14, "overbought": 70, "oversold": 30, "optimized_ranges": {
        "Forex": {"long": [50, 68], "short": [32, 50]},
        "Oro": {"long": [45, 72], "short": [28, 55]},
        "Indices": {"long": [52, 70], "short": [30, 48]},
    }},
    "MACD": {"fast_period": 12, "slow_period": 26, "signal_period": 9},
    "BollingerBands": {"period": 20, "std_dev": 2, "oro_std_dev": 2.5}, # BB (20, 2.5) para Oro
    "ATR": {"period": 14},
    "ADX": {"period": 14, "threshold_forex": 20, "threshold_indices_oro": 18}, # Ajustado según recomendación
    "VWAP": {"period": "daily"},
    "Ichimoku": {},
    "VIX": {},
    "DXY": {},
}

# --- Reglas de Entrada ---

ENTRY_RULES_LONG = [
    "Precio > EMA200",
    "EMA50 > EMA200",
    "EMA20 > EMA50",
    "EMA9 > EMA20",
    "MACD bullish crossover",
    "Histograma MACD positivo",
    "RSI validado",
    "ADX validado",
    "Confirmación de vela japonesa",
    "Confirmación soporte/resistencia",
    "Confirmación VWAP",
    "Tendencia HTF alineada",
]

ENTRY_RULES_SHORT = [
    # Condiciones inversas para venta
]

# --- Gestión de Riesgo ---

TP_RATIOS = {
    "TP1": 3,
    "TP2": 6,
    "TP3": 10,
}

SL_MULTIPLIER_ATR = {
    "Forex": 1.0, # ATR x multiplicador
    "Indices": 1.0, # ATR o estructura
    "Oro": 1.5, # ATR amplio + estructura
}

# --- Integración Telegram ---

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "8630459101:AAE3-qhxqrxhgL3gfeJD2j-_vlxlrLcXUcg")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "1288556160")
TELEGRAM_DAILY_MESSAGE_TIME = "09:00"

# --- Integración Gmail ---

GMAIL_CLIENT_SECRET_PATH = os.getenv("GMAIL_CLIENT_SECRET_PATH", "client_secret.json")
GMAIL_SENDER_EMAIL = os.getenv("GMAIL_SENDER_EMAIL", "toledomendizabal.invertision@gmail.com")
GMAIL_RECIPIENT_EMAIL = os.getenv("GMAIL_RECIPIENT_EMAIL", "toledomendizabal.invertision@gmail.com")
DAILY_REPORT_TIME = "23:59"

# --- Integración Twelve Data (Respaldo) ---

TWELVEDATA_API_KEY = os.getenv("TWELVEDATA_API_KEY", "e046f5d7b689457fb44308ef76dc434c")

# --- Configuración de Base de Datos ---

DATABASE_URL = "sqlite:///./data/sisetrweb.db" # Usaremos SQLite por simplicidad inicial

# --- Configuración de Logs ---

LOGS_DIR = "logs"
SYSTEM_LOG_FILE = os.path.join(LOGS_DIR, "system.log")
SIGNALS_LOG_FILE = os.path.join(LOGS_DIR, "signals.log")
MONITORING_LOG_FILE = os.path.join(LOGS_DIR, "monitoring.log")
BACKTESTING_LOG_FILE = os.path.join(LOGS_DIR, "backtesting.log")

# --- Dashboard ---

DASHBOARD_REFRESH_INTERVAL_SECONDS = 10

# --- Excel Autogestionado ---

EXCEL_SIGNALS_FILE = "data/signals.xlsx"
EXCEL_SETTINGS_FILE = "data/settings.xlsx"
EXCEL_BACKTESTING_FILE = "data/backtesting.xlsx"

