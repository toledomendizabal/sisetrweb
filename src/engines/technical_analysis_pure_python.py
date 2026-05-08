"""
SISETRWEB - Motor de Análisis Técnico (Python Puro)
Versión 100% Python sin dependencias compiladas (numba, talib, pandas-ta)
Compatible con Python 3.14+

Este módulo proporciona indicadores técnicos implementados directamente en Python
sin depender de librerías compiladas que pueden causar problemas de compatibilidad.
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
        """
        Inicializa el motor de análisis técnico.

        Args:
            lookback_periods: Diccionario con períodos de lookback para cada indicador
        """
        self.lookback_periods = lookback_periods or {
            'rsi': 14,
            'macd': 12,
            'bb': 20,
            'atr': 14,
            'stoch': 14,
            'ema': 20,
            'sma': 50,
            'adx': 14
        }

    def calculate_rsi(self, prices: np.ndarray, period: int = 14) -> np.ndarray:
        """
        Calcula el Índice de Fuerza Relativa (RSI).
        Implementación en Python puro sin dependencias externas.

        Args:
            prices: Array de precios de cierre
            period: Período de cálculo (default: 14)

        Returns:
            Array con valores RSI (0-100)
        """
        try:
            if len(prices) < period + 1:
                return np.zeros_like(prices)

            rsi = np.zeros_like(prices, dtype=float)
            deltas = np.diff(prices)
            seed = deltas[:period + 1]
            
            up = seed[seed >= 0].sum() / period
            down = -seed[seed < 0].sum() / period
            
            rs = up / down if down != 0 else 0
            rsi[period] = 100.0 - 100.0 / (1.0 + rs)
            
            for i in range(period + 1, len(prices)):
                delta = deltas[i - 1]
                if delta > 0:
                    upval = delta
                    downval = 0.0
                else:
                    upval = 0.0
                    downval = -delta
                
                up = (up * (period - 1) + upval) / period
                down = (down * (period - 1) + downval) / period
                
                rs = up / down if down != 0 else 0
                rsi[i] = 100.0 - 100.0 / (1.0 + rs)
            
            return rsi
        except Exception as e:
            logger.error(f"Error calculando RSI: {e}")
            return np.zeros_like(prices)

    def calculate_macd(self, prices: np.ndarray, fast: int = 12, slow: int = 26, signal: int = 9) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Calcula MACD (Moving Average Convergence Divergence).

        Args:
            prices: Array de precios de cierre
            fast: Período EMA rápido (default: 12)
            slow: Período EMA lento (default: 26)
            signal: Período de la línea de señal (default: 9)

        Returns:
            Tupla (macd, signal, histogram)
        """
        try:
            ema_fast = self._calculate_ema_internal(prices, fast)
            ema_slow = self._calculate_ema_internal(prices, slow)
            macd_line = ema_fast - ema_slow
            signal_line = self._calculate_ema_internal(macd_line, signal)
            histogram = macd_line - signal_line
            
            return macd_line, signal_line, histogram
        except Exception as e:
            logger.error(f"Error calculando MACD: {e}")
            return np.zeros_like(prices), np.zeros_like(prices), np.zeros_like(prices)

    def calculate_bollinger_bands(self, prices: np.ndarray, period: int = 20, std_dev: float = 2.0) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Calcula las Bandas de Bollinger.

        Args:
            prices: Array de precios de cierre
            period: Período de la media móvil (default: 20)
            std_dev: Número de desviaciones estándar (default: 2.0)

        Returns:
            Tupla (banda_superior, media, banda_inferior)
        """
        try:
            middle = self._calculate_sma_internal(prices, period)
            
            # Calcular desviación estándar
            std = np.zeros_like(prices, dtype=float)
            for i in range(period - 1, len(prices)):
                std[i] = np.std(prices[i - period + 1:i + 1])
            
            upper = middle + (std_dev * std)
            lower = middle - (std_dev * std)
            
            return upper, middle, lower
        except Exception as e:
            logger.error(f"Error calculando Bollinger Bands: {e}")
            return np.zeros_like(prices), np.zeros_like(prices), np.zeros_like(prices)

    def calculate_atr(self, high: np.ndarray, low: np.ndarray, close: np.ndarray, period: int = 14) -> np.ndarray:
        """
        Calcula el Rango Verdadero Promedio (ATR).

        Args:
            high: Array de precios máximos
            low: Array de precios mínimos
            close: Array de precios de cierre
            period: Período de cálculo (default: 14)

        Returns:
            Array con valores ATR
        """
        try:
            # Calcular Rango Verdadero (TR)
            tr = np.zeros_like(close, dtype=float)
            
            for i in range(1, len(close)):
                tr1 = high[i] - low[i]
                tr2 = abs(high[i] - close[i - 1])
                tr3 = abs(low[i] - close[i - 1])
                tr[i] = max(tr1, tr2, tr3)
            
            # Calcular ATR como promedio móvil del TR
            atr = self._calculate_ema_internal(tr, period)
            return atr
        except Exception as e:
            logger.error(f"Error calculando ATR: {e}")
            return np.zeros_like(close)

    def calculate_stochastic(self, high: np.ndarray, low: np.ndarray, close: np.ndarray, period: int = 14, smooth_k: int = 3, smooth_d: int = 3) -> Tuple[np.ndarray, np.ndarray]:
        """
        Calcula el Oscilador Estocástico.

        Args:
            high: Array de precios máximos
            low: Array de precios mínimos
            close: Array de precios de cierre
            period: Período de cálculo (default: 14)
            smooth_k: Período de suavizado K (default: 3)
            smooth_d: Período de suavizado D (default: 3)

        Returns:
            Tupla (K, D)
        """
        try:
            k = np.zeros_like(close, dtype=float)
            
            for i in range(period - 1, len(close)):
                lowest_low = np.min(low[i - period + 1:i + 1])
                highest_high = np.max(high[i - period + 1:i + 1])
                
                if highest_high != lowest_low:
                    k[i] = 100 * (close[i] - lowest_low) / (highest_high - lowest_low)
                else:
                    k[i] = 50
            
            # Suavizar K
            k_smooth = self._calculate_sma_internal(k, smooth_k)
            
            # Calcular D como SMA de K suavizado
            d = self._calculate_sma_internal(k_smooth, smooth_d)
            
            return k_smooth, d
        except Exception as e:
            logger.error(f"Error calculando Estocástico: {e}")
            return np.zeros_like(close), np.zeros_like(close)

    def calculate_ema(self, prices: np.ndarray, period: int = 20) -> np.ndarray:
        """
        Calcula la Media Móvil Exponencial (EMA).

        Args:
            prices: Array de precios de cierre
            period: Período de cálculo (default: 20)

        Returns:
            Array con valores EMA
        """
        return self._calculate_ema_internal(prices, period)

    def calculate_sma(self, prices: np.ndarray, period: int = 50) -> np.ndarray:
        """
        Calcula la Media Móvil Simple (SMA).

        Args:
            prices: Array de precios de cierre
            period: Período de cálculo (default: 50)

        Returns:
            Array con valores SMA
        """
        return self._calculate_sma_internal(prices, period)

    def calculate_adx(self, high: np.ndarray, low: np.ndarray, close: np.ndarray, period: int = 14) -> np.ndarray:
        """
        Calcula el Índice Direccional Promedio (ADX).

        Args:
            high: Array de precios máximos
            low: Array de precios mínimos
            close: Array de precios de cierre
            period: Período de cálculo (default: 14)

        Returns:
            Array con valores ADX
        """
        try:
            # Calcular movimientos direccionales
            up_move = np.zeros_like(high, dtype=float)
            down_move = np.zeros_like(low, dtype=float)
            
            for i in range(1, len(high)):
                up_move[i] = high[i] - high[i - 1]
                down_move[i] = low[i - 1] - low[i]
            
            # Determinar movimientos positivos y negativos
            plus_dm = np.where((up_move > down_move) & (up_move > 0), up_move, 0)
            minus_dm = np.where((down_move > up_move) & (down_move > 0), down_move, 0)
            
            # Calcular ATR
            atr = self.calculate_atr(high, low, close, period)
            
            # Calcular DI+, DI-
            di_plus = 100 * self._calculate_ema_internal(plus_dm, period) / (atr + 1e-10)
            di_minus = 100 * self._calculate_ema_internal(minus_dm, period) / (atr + 1e-10)
            
            # Calcular DX
            dx = 100 * np.abs(di_plus - di_minus) / (di_plus + di_minus + 1e-10)
            
            # Calcular ADX como EMA de DX
            adx = self._calculate_ema_internal(dx, period)
            
            return adx
        except Exception as e:
            logger.error(f"Error calculando ADX: {e}")
            return np.zeros_like(close)

    def calculate_all_indicators(self, ohlcv_data: Dict[str, np.ndarray]) -> Dict[str, np.ndarray]:
        """
        Calcula todos los indicadores técnicos disponibles.

        Args:
            ohlcv_data: Diccionario con claves 'open', 'high', 'low', 'close', 'volume'

        Returns:
            Diccionario con todos los indicadores calculados
        """
        indicators = {}

        try:
            close = ohlcv_data.get('close', np.array([]))
            high = ohlcv_data.get('high', np.array([]))
            low = ohlcv_data.get('low', np.array([]))

            # Indicadores de momentum
            indicators['rsi'] = self.calculate_rsi(close, self.lookback_periods['rsi'])
            indicators['macd'], indicators['macd_signal'], indicators['macd_histogram'] = self.calculate_macd(close)

            # Indicadores de volatilidad
            indicators['bb_upper'], indicators['bb_middle'], indicators['bb_lower'] = self.calculate_bollinger_bands(
                close, self.lookback_periods['bb']
            )
            indicators['atr'] = self.calculate_atr(high, low, close, self.lookback_periods['atr'])

            # Indicadores de tendencia
            indicators['ema'] = self.calculate_ema(close, self.lookback_periods['ema'])
            indicators['sma'] = self.calculate_sma(close, self.lookback_periods['sma'])
            indicators['adx'] = self.calculate_adx(high, low, close, self.lookback_periods['adx'])

            # Osciladores
            indicators['stoch_k'], indicators['stoch_d'] = self.calculate_stochastic(
                high, low, close, self.lookback_periods['stoch']
            )

            logger.info("Todos los indicadores técnicos calculados exitosamente")
            return indicators

        except Exception as e:
            logger.error(f"Error calculando indicadores técnicos: {e}")
            return {}

    def detect_divergence(self, prices: np.ndarray, rsi: np.ndarray, window: int = 14) -> Dict[str, bool]:
        """
        Detecta divergencias entre precio y RSI.

        Args:
            prices: Array de precios de cierre
            rsi: Array de valores RSI
            window: Ventana de análisis (default: 14)

        Returns:
            Diccionario con divergencias detectadas
        """
        divergences = {
            'bullish_divergence': False,
            'bearish_divergence': False
        }

        try:
            if len(prices) < window or len(rsi) < window:
                return divergences

            # Detectar divergencia alcista (precio bajo, RSI alto)
            if prices[-1] < prices[-window] and rsi[-1] > rsi[-window]:
                divergences['bullish_divergence'] = True

            # Detectar divergencia bajista (precio alto, RSI bajo)
            if prices[-1] > prices[-window] and rsi[-1] < rsi[-window]:
                divergences['bearish_divergence'] = True

            return divergences

        except Exception as e:
            logger.error(f"Error detectando divergencias: {e}")
            return divergences

    # ========================================================================
    # MÉTODOS INTERNOS (Implementaciones de indicadores base)
    # ========================================================================

    def _calculate_ema_internal(self, prices: np.ndarray, period: int) -> np.ndarray:
        """Calcula EMA internamente"""
        if len(prices) < period:
            return np.zeros_like(prices)
        
        ema = np.zeros_like(prices, dtype=float)
        multiplier = 2.0 / (period + 1)
        
        # SMA inicial
        ema[period - 1] = np.mean(prices[:period])
        
        # EMA
        for i in range(period, len(prices)):
            ema[i] = prices[i] * multiplier + ema[i - 1] * (1 - multiplier)
        
        return ema

    def _calculate_sma_internal(self, prices: np.ndarray, period: int) -> np.ndarray:
        """Calcula SMA internamente"""
        if len(prices) < period:
            return np.zeros_like(prices)
        
        sma = np.zeros_like(prices, dtype=float)
        
        for i in range(period - 1, len(prices)):
            sma[i] = np.mean(prices[i - period + 1:i + 1])
        
        return sma
