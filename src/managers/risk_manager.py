
from config.settings import SL_MULTIPLIER_ATR, TP_RATIOS, ASSETS_CONFIG

def calculate_lot_size(capital, risk_percent, sl_pips):
    """Calcula el tamaño del lote basado en el riesgo y la distancia del Stop Loss."""
    if sl_pips == 0: return 0.01
    
    risk_amount = capital * risk_percent
    # Valor por pip simplificado (ej. 10 USD para 1 lote estándar en EURUSD)
    pip_value = 10 
    lot_size = risk_amount / (sl_pips * pip_value)
    
    return round(max(0.01, lot_size), 2)

def calculate_tp_sl(asset, entry_price, atr, signal_type):
    """Calcula los niveles de Take Profit y Stop Loss."""
    asset_group = ASSETS_CONFIG[asset]["group"]
    multiplier = SL_MULTIPLIER_ATR.get(asset_group, 1.0)
    
    sl_distance = atr * multiplier
    
    if signal_type == "BUY":
        sl = entry_price - sl_distance
        tp1 = entry_price + (sl_distance * TP_RATIOS["TP1"])
        tp2 = entry_price + (sl_distance * TP_RATIOS["TP2"])
        tp3 = entry_price + (sl_distance * TP_RATIOS["TP3"])
    else:
        sl = entry_price + sl_distance
        tp1 = entry_price - (sl_distance * TP_RATIOS["TP1"])
        tp2 = entry_price - (sl_distance * TP_RATIOS["TP2"])
        tp3 = entry_price - (sl_distance * TP_RATIOS["TP3"])
        
    return sl, tp1, tp2, tp3

