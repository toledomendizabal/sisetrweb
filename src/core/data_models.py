
from pydantic import BaseModel
from datetime import datetime
from typing import List, Dict, Any, Optional

class Signal(BaseModel):
    asset: str
    type: str  # BUY/SELL
    entry_price: float
    stop_loss: float
    tp1: float
    tp2: float
    tp3: float
    sl_distance_pips: float
    tp_distance_pips: float
    lot_size: float
    timeframe: str
    timestamp: datetime
    indicators_met: List[str]
    score: str
    status: str = "ACTIVE" # ACTIVE, TP1, TP2, TP3, SL, CLOSED
    pnl: Optional[float] = None

class BacktestingResult(BaseModel):
    asset: str
    win_rate: float
    profit_factor: float
    drawdown: float
    expectancy: float
    sharpe_ratio: float
    recommendations: List[str]
    timestamp: datetime

class AssetConfig(BaseModel):
    enabled: bool
    group: str
    timeframe_signal: List[str]
    timeframe_trend: List[str]
    rsi_long_range: Optional[List[int]] = None
    rsi_short_range: Optional[List[int]] = None
    adx_threshold: Optional[int] = None
    sl_atr_multiplier: Optional[float] = None

class IndicatorConfig(BaseModel):
    ema_periods: Optional[List[int]] = None
    rsi_period: Optional[int] = None
    macd_fast_period: Optional[int] = None
    macd_slow_period: Optional[int] = None
    macd_signal_period: Optional[int] = None
    bollinger_period: Optional[int] = None
    bollinger_std_dev: Optional[float] = None
    atr_period: Optional[int] = None
    adx_period: Optional[int] = None

class SystemConfig(BaseModel):
    capital_base: float
    risk_per_trade_percent: float
    monitoring_interval_seconds: int
    assets: Dict[str, AssetConfig]
    indicators: IndicatorConfig


