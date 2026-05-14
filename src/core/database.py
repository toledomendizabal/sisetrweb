
import sqlite3
import os
from datetime import datetime
import json
from config.settings import DATABASE_URL
from src.core.data_models import Signal, BacktestingResult
from src.core.logger import setup_logging

logger = setup_logging()

def get_db_connection():
    db_path = DATABASE_URL.replace("sqlite:///", "")
    db_dir = os.path.dirname(db_path)
    if db_dir and not os.path.exists(db_dir):
        os.makedirs(db_dir, exist_ok=True)
        logger.info(f"Directorio de base de datos creado: {db_dir}")
    
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row # Permite acceder a las columnas por nombre
    return conn

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS signals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            asset TEXT NOT NULL,
            type TEXT NOT NULL,
            entry_price REAL NOT NULL,
            stop_loss REAL NOT NULL,
            tp1 REAL NOT NULL,
            tp2 REAL NOT NULL,
            tp3 REAL NOT NULL,
            sl_distance_pips REAL NOT NULL,
            tp_distance_pips REAL NOT NULL,
            lot_size REAL NOT NULL,
            timeframe TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            indicators_met TEXT NOT NULL,
            score TEXT NOT NULL,
            status TEXT NOT NULL,
            pnl REAL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS backtesting_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            asset TEXT NOT NULL,
            win_rate REAL NOT NULL,
            profit_factor REAL NOT NULL,
            drawdown REAL NOT NULL,
            expectancy REAL NOT NULL,
            sharpe_ratio REAL NOT NULL,
            recommendations TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    logger.info("Tablas de base de datos creadas o verificadas.")

def insert_signal(signal: Signal):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO signals (asset, type, entry_price, stop_loss, tp1, tp2, tp3, sl_distance_pips, tp_distance_pips, lot_size, timeframe, timestamp, indicators_met, score, status, pnl)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        signal.asset, signal.type, signal.entry_price, signal.stop_loss, signal.tp1, signal.tp2, signal.tp3,
        signal.sl_distance_pips, signal.tp_distance_pips, signal.lot_size, signal.timeframe, signal.timestamp.isoformat(),
        json.dumps(signal.indicators_met), signal.score, signal.status, signal.pnl
    ))
    conn.commit()
    conn.close()
    logger.info(f"Señal insertada para {signal.asset}")

def get_active_signals():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM signals WHERE status = 'ACTIVE'")
    rows = cursor.fetchall()
    conn.close()
    return [Signal(**{k: (json.loads(v) if k == 'indicators_met' else (datetime.fromisoformat(v) if k == 'timestamp' else v)) for k, v in row.items()}) for row in rows]

def update_signal_status(signal_id: int, status: str, pnl: float = None):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE signals SET status = ?, pnl = ? WHERE id = ?", (status, pnl, signal_id))
    conn.commit()
    conn.close()
    logger.info(f"Señal {signal_id} actualizada a estado {status}")

def insert_backtesting_result(result: BacktestingResult):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO backtesting_results (asset, win_rate, profit_factor, drawdown, expectancy, sharpe_ratio, recommendations, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        result.asset, result.win_rate, result.profit_factor, result.drawdown, result.expectancy, result.sharpe_ratio,
        json.dumps(result.recommendations), result.timestamp.isoformat()
    ))
    conn.commit()
    conn.close()
    logger.info(f"Resultado de backtesting insertado para {result.asset}")

