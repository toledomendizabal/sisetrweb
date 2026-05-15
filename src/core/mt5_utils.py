
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

def is_position_open(symbol):
    """Verifica si hay una posición abierta para el símbolo dado."""
    positions = mt5.positions_get(symbol=symbol)
    if positions is None:
        logger.error(f"Error al obtener posiciones para {symbol}: {mt5.last_error()}")
        return False
    return len(positions) > 0

def get_position_pnl(symbol):
    """Obtiene el PnL actual de la posición abierta para el símbolo."""
    positions = mt5.positions_get(symbol=symbol)
    if positions and len(positions) > 0:
        return positions[0].profit
    return 0.0

def get_last_closed_position_details(symbol):
    """Obtiene los detalles de la última posición cerrada para un símbolo."""
    import time
    # Obtener historial de las últimas 24 horas
    from_date = time.time() - 24 * 60 * 60
    to_date = time.time() + 60
    
    history = mt5.history_deals_get(from_date, to_date, group=f"*{symbol}*")
    if history is None or len(history) == 0:
        return None
    
    # Filtrar solo los deals que cierran una posición (entry out)
    # DEAL_ENTRY_OUT = 1
    closed_deals = [d for d in history if d.entry == 1]
    if not closed_deals:
        return None
    
    # Tomar el último deal de cierre
    last_deal = closed_deals[-1]
    
    # Determinar si fue SL o TP basándose en el comentario o el precio
    # Nota: MT5 suele poner [sl] o [tp] en el comentario del deal
    comment = last_deal.comment.lower()
    status = "CLOSED"
    if "sl" in comment:
        status = "STOP LOSS"
    elif "tp" in comment:
        status = "TAKE PROFIT"
    
    return {
        "status": status,
        "pnl": last_deal.profit + last_deal.commission + last_deal.swap,
        "price": last_deal.price,
        "time": datetime.fromtimestamp(last_deal.time)
    }

