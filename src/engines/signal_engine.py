
from datetime import datetime
from src.core.data_models import Signal
from src.engines.technical_analysis import calculate_indicators, calculate_signal_score, detect_candlestick_patterns
from src.managers.risk_manager import calculate_lot_size, calculate_tp_sl
from config.settings import ASSETS_CONFIG, INDICATORS_CONFIG, CAPITAL_BASE, RIESGO_POR_OPERACION_PERCENT

def evaluate_signal(asset, df_signal, df_trend):
    """Evalúa si se cumplen las condiciones para generar una señal."""
    if df_signal is None or df_trend is None:
        return None

    df_signal = calculate_indicators(df_signal)
    df_trend = calculate_indicators(df_trend)

    latest_signal = df_signal.iloc[-1]
    latest_trend = df_trend.iloc[-1]
    
    indicators_met = []
    
    # --- Reglas de Compra (Long) ---
    # 1. Tendencia Macro (EMA 200)
    if latest_trend["close"] > latest_trend["EMA_200"]:
        indicators_met.append("Trend Macro Bullish")
    
    # 2. Alineación de EMAs
    if latest_signal["EMA_50"] > latest_signal["EMA_200"] and \
       latest_signal["EMA_20"] > latest_signal["EMA_50"] and \
       latest_signal["EMA_9"] > latest_signal["EMA_20"]:
        indicators_met.append("EMAs Aligned Bullish")

    # 3. MACD
    if latest_signal["MACD"] > latest_signal["MACD_Signal"] and latest_signal["MACD_Hist"] > 0:
        indicators_met.append("MACD Bullish")

    # 4. RSI
    asset_group = ASSETS_CONFIG[asset]["group"]
    rsi_range = INDICATORS_CONFIG["RSI"]["optimized_ranges"][asset_group]["long"]
    if rsi_range[0] <= latest_signal["RSI"] <= rsi_range[1]:
        indicators_met.append("RSI Validated")

    # 5. ADX
    threshold = INDICATORS_CONFIG["ADX"]["threshold_forex"] if asset_group == "Forex" else INDICATORS_CONFIG["ADX"]["threshold_indices_oro"]
    if latest_signal["ADX"] > threshold:
        indicators_met.append("ADX Validated")

    # 6. Patrones de Velas
    patterns = detect_candlestick_patterns(df_signal)
    if patterns:
        indicators_met.append(f"Candlestick: {', '.join(patterns)}")

    # 7. VWAP
    if latest_signal["close"] > latest_signal["VWAP"]:
        indicators_met.append("Above VWAP")

    # Calcular Score
    score = calculate_signal_score(indicators_met)
    
    if score != "REJECTED":
        # Calcular TP y SL
        entry_price = latest_signal["close"]
        atr = latest_signal["ATR"]
        sl, tp1, tp2, tp3 = calculate_tp_sl(asset, entry_price, atr, "BUY")
        
        # Calcular Lotaje
        sl_pips = abs(entry_price - sl) * 10000 # Simplificado para Forex
        lot_size = calculate_lot_size(CAPITAL_BASE, RIESGO_POR_OPERACION_PERCENT, sl_pips)

        return Signal(
            asset=asset,
            type="BUY",
            entry_price=entry_price,
            stop_loss=sl,
            tp1=tp1,
            tp2=tp2,
            tp3=tp3,
            sl_distance_pips=sl_pips,
            tp_distance_pips=abs(tp1 - entry_price) * 10000,
            lot_size=lot_size,
            timeframe="5M", # Ejemplo
            timestamp=datetime.now(),
            indicators_met=indicators_met,
            score=score
        )

    return None

