
import pandas as pd
import talib
import numpy as np
from config.settings import INDICATORS_CONFIG

def calculate_indicators(df):
    """Calcula todos los indicadores técnicos necesarios."""
    if df is None or df.empty:
        return None

    # EMA
    for period in INDICATORS_CONFIG["EMA"]["periods"]:
        df[f"EMA_{period}"] = talib.EMA(df["close"], timeperiod=period)

    # RSI
    df["RSI"] = talib.RSI(df["close"], timeperiod=INDICATORS_CONFIG["RSI"]["period"])

    # MACD
    macd, macdsignal, macdhist = talib.MACD(
        df["close"],
        fastperiod=INDICATORS_CONFIG["MACD"]["fast_period"],
        slowperiod=INDICATORS_CONFIG["MACD"]["slow_period"],
        signalperiod=INDICATORS_CONFIG["MACD"]["signal_period"]
    )
    df["MACD"] = macd
    df["MACD_Signal"] = macdsignal
    df["MACD_Hist"] = macdhist

    # Bollinger Bands
    upper, middle, lower = talib.BBANDS(
        df["close"],
        timeperiod=INDICATORS_CONFIG["BollingerBands"]["period"],
        nbdevup=INDICATORS_CONFIG["BollingerBands"]["std_dev"],
        nbdevdn=INDICATORS_CONFIG["BollingerBands"]["std_dev"],
        matype=0
    )
    df["BB_Upper"] = upper
    df["BB_Middle"] = middle
    df["BB_Lower"] = lower

    # ATR
    df["ATR"] = talib.ATR(df["high"], df["low"], df["close"], timeperiod=INDICATORS_CONFIG["ATR"]["period"])

    # ADX
    df["ADX"] = talib.ADX(df["high"], df["low"], df["close"], timeperiod=INDICATORS_CONFIG["ADX"]["period"])

    # VWAP (Simplificado: Precio promedio ponderado por volumen acumulado diario)
    # En un entorno real, esto se calcularía con datos intradía acumulados desde el inicio del día
    df["VWAP"] = (df["close"] * df["tick_volume"]).cumsum() / df["tick_volume"].cumsum()

    return df

def detect_divergence(df, period=14):
    """Detecta divergencias entre el precio y el RSI."""
    # Implementación simplificada de detección de divergencias
    # Se buscarían mínimos más bajos en el precio y mínimos más altos en el RSI (alcista)
    # O máximos más altos en el precio y máximos más bajos en el RSI (bajista)
    return "None" # Placeholder

def detect_candlestick_patterns(df):
    """Detecta patrones de velas japonesas."""
    patterns = []
    
    # Bullish Engulfing
    res = talib.CDLENGULFING(df["open"], df["high"], df["low"], df["close"])
    if res.iloc[-1] > 0: patterns.append("Bullish Engulfing")
    elif res.iloc[-1] < 0: patterns.append("Bearish Engulfing")

    # Hammer
    res = talib.CDLHAMMER(df["open"], df["high"], df["low"], df["close"])
    if res.iloc[-1] > 0: patterns.append("Hammer")

    # Shooting Star
    res = talib.CDLSHOOTINGSTAR(df["open"], df["high"], df["low"], df["close"])
    if res.iloc[-1] > 0: patterns.append("Shooting Star")

    return patterns

def calculate_signal_score(indicators_met):
    """Calcula el score de la señal basado en el número de indicadores cumplidos."""
    count = len(indicators_met)
    if count >= 12: return "AAA"
    if count >= 10: return "AA"
    if count >= 8: return "A"
    return "REJECTED"

