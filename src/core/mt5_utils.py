
import MetaTrader5 as mt5
from datetime import datetime
import pytz
import pandas as pd
from src.core.logger import setup_logging

logger = setup_logging()

def initialize_mt5():
    if not mt5.initialize():
        logger.error(f"MetaTrader5 initialization failed: {mt5.last_error()}")
        return False
    logger.info("MetaTrader5 inicializado correctamente.")
    return True

def shutdown_mt5():
    mt5.shutdown()
    logger.info("MetaTrader5 desconectado.")

def get_ohlc_data(symbol, timeframe, count):
    if not mt5.symbol_info(symbol):
        logger.error(f"Símbolo {symbol} no encontrado en MetaTrader5.")
        return None

    utc_from = datetime.now(pytz.utc) - pd.Timedelta(minutes=timeframe_to_minutes(timeframe) * count * 2) # Obtener el doble de datos para asegurar suficientes
    # Mapeo correcto de timeframes para MetaTrader5
    mt5_timeframe = {
        "1M": mt5.TIMEFRAME_M1,
        "3M": mt5.TIMEFRAME_M3,
        "5M": mt5.TIMEFRAME_M5,
        "15M": mt5.TIMEFRAME_M15,
        "30M": mt5.TIMEFRAME_M30,
        "1H": mt5.TIMEFRAME_H1,
        "4H": mt5.TIMEFRAME_H4,
        "1D": mt5.TIMEFRAME_D1
    }.get(timeframe)

    if mt5_timeframe is None:
        logger.error(f"Timeframe {timeframe} no soportado por MetaTrader5.")
        return None

    rates = mt5.copy_rates_from(symbol, mt5_timeframe, utc_from, count * 2)

    if rates is None:
        logger.error(f"No se pudieron obtener datos OHLC para {symbol} en {timeframe}: {mt5.last_error()}")
        return None

    if len(rates) == 0:
        logger.warning(f"No hay datos OHLC disponibles para {symbol} en {timeframe}.")
        return None

    df = pd.DataFrame(rates)
    df["time"] = pd.to_datetime(df["time"], unit="s")
    df = df.set_index("time")
    df = df.iloc[-count:] # Tomar solo los últimos 'count' datos

    return df

def timeframe_to_minutes(timeframe_str):
    if timeframe_str == "1M": return 1
    if timeframe_str == "3M": return 3
    if timeframe_str == "5M": return 5
    if timeframe_str == "15M": return 15
    if timeframe_str == "30M": return 30
    if timeframe_str == "1H": return 60
    if timeframe_str == "4H": return 240
    if timeframe_str == "1D": return 1440
    return 1 # Default

