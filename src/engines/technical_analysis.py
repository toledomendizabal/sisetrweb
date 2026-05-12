
"""
SISETRWEB - Motor de Análisis Técnico (Python Puro)
Versión 100% Python sin dependencias compiladas (numba, talib, pandas-ta)
Compatible con Python 3.14+
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Tuple, Optional
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class TechnicalAnalysisEngine:
    """Motor de análisis técnico en Python puro"""

    def __init__(self, lookback_periods: Dict[str, int] = None):
        self.lookback_periods = lookback_periods or {
            'rsi': 14, 'macd': 12, 'bb': 20, 'atr': 14,
            'stoch': 14, 'ema': 20, 'sma': 50, 'adx': 14
        }

    def calculate_rsi(self, prices: np.ndarray, period: int = 14) -> np.ndarray:
        try:
            if len(prices) < period + 1: return np.zeros_like(prices)
            rsi = np.zeros_like(prices, dtype=float)
            deltas = np.diff(prices)
            seed = deltas[:period]
            up = seed[seed >= 0].sum() / period
            down = -seed[seed < 0].sum() / period
            rs = up / down if down != 0 else 0
            rsi[period] = 100.0 - 100.0 / (1.0 + rs)
            for i in range(period + 1, len(prices)):
                delta = deltas[i - 1]
                upval = delta if delta > 0 else 0.0
                downval = -delta if delta < 0 else 0.0
                up = (up * (period - 1) + upval) / period
                down = (down * (period - 1) + downval) / period
                rs = up / down if down != 0 else 0
                rsi[i] = 100.0 - 100.0 / (1.0 + rs)
            return rsi
        except Exception as e:
            logger.error(f"Error calculando RSI: {e}")
            return np.zeros_like(prices)

    def calculate_macd(self, prices: np.ndarray, fast: int = 12, slow: int = 26, signal: int = 9) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        ema_fast = self._calculate_ema_internal(prices, fast)
        ema_slow = self._calculate_ema_internal(prices, slow)
        macd_line = ema_fast - ema_slow
        signal_line = self._calculate_ema_internal(macd_line, signal)
        histogram = macd_line - signal_line
        return macd_line, signal_line, histogram

    def calculate_atr(self, high: np.ndarray, low: np.ndarray, close: np.ndarray, period: int = 14) -> np.ndarray:
        tr = np.zeros_like(close, dtype=float)
        for i in range(1, len(close)):
            tr[i] = max(high[i] - low[i], abs(high[i] - close[i-1]), abs(low[i] - close[i-1]))
        return self._calculate_ema_internal(tr, period)

    def calculate_adx(self, high: np.ndarray, low: np.ndarray, close: np.ndarray, period: int = 14) -> np.ndarray:
        up_move = np.zeros_like(high)
        down_move = np.zeros_like(low)
        for i in range(1, len(high)):
            up_move[i] = high[i] - high[i-1]
            down_move[i] = low[i-1] - low[i]
        plus_dm = np.where((up_move > down_move) & (up_move > 0), up_move, 0)
        minus_dm = np.where((down_move > up_move) & (down_move > 0), down_move, 0)
        atr = self.calculate_atr(high, low, close, period)
        di_plus = 100 * self._calculate_ema_internal(plus_dm, period) / (atr + 1e-10)
        di_minus = 100 * self._calculate_ema_internal(minus_dm, period) / (atr + 1e-10)
        dx = 100 * np.abs(di_plus - di_minus) / (di_plus + di_minus + 1e-10)
        return self._calculate_ema_internal(dx, period)

    def _calculate_ema_internal(self, prices: np.ndarray, period: int) -> np.ndarray:
        if len(prices) < period: return np.zeros_like(prices)
        ema = np.zeros_like(prices, dtype=float)
        multiplier = 2.0 / (period + 1)
        ema[period - 1] = np.mean(prices[:period])
        for i in range(period, len(prices)):
            ema[i] = (prices[i] - ema[i-1]) * multiplier + ema[i-1]
        return ema

# --- Funciones de conveniencia para signal_engine.py ---

def calculate_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula todos los indicadores necesarios para el DataFrame."""
    engine = TechnicalAnalysisEngine()
    close = df['close'].values
    high = df['high'].values
    low = df['low'].values
    
    df['EMA_9'] = engine._calculate_ema_internal(close, 9)
    df['EMA_20'] = engine._calculate_ema_internal(close, 20)
    df['EMA_50'] = engine._calculate_ema_internal(close, 50)
    df['EMA_200'] = engine._calculate_ema_internal(close, 200)
    
    macd, signal, hist = engine.calculate_macd(close)
    df['MACD'] = macd
    df['MACD_Signal'] = signal
    df['MACD_Hist'] = hist
    
    df['RSI'] = engine.calculate_rsi(close, 14)
    df['ADX'] = engine.calculate_adx(high, low, close, 14)
    df['ATR'] = engine.calculate_atr(high, low, close, 14)
    
    # VWAP Simplificado (Precio Típico acumulado por volumen)
    typical_price = (df['high'] + df['low'] + df['close']) / 3
    df['VWAP'] = (typical_price * df['tick_volume']).cumsum() / df['tick_volume'].cumsum()
    
    return df

def calculate_signal_score(indicators_met: List[str]) -> str:
    """Calcula el score de la señal basado en los indicadores cumplidos."""
    score = len(indicators_met)
    if score >= 5:
        return "STRONG"
    elif score >= 3:
        return "WEAK"
    else:
        return "REJECTED"

def detect_candlestick_patterns(df: pd.DataFrame) -> List[str]:
    """Detecta patrones de velas básicos."""
    patterns = []
    if len(df) < 3: return patterns
    
    last = df.iloc[-1]
    prev = df.iloc[-2]
    
    # Engulfing Bullish
    if last['close'] > last['open'] and prev['close'] < prev['open'] and \
       last['close'] > prev['open'] and last['open'] < prev['close']:
        patterns.append("Bullish Engulfing")
        
    # Hammer
    body = abs(last['close'] - last['open'])
    lower_shadow = min(last['open'], last['close']) - last['low']
    upper_shadow = last['high'] - max(last['open'], last['close'])
    if lower_shadow > 2 * body and upper_shadow < body:
        patterns.append("Hammer")
        
    return patterns
