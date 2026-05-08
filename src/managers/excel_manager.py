
import pandas as pd
import os
from openpyxl import load_workbook
from config.settings import EXCEL_SIGNALS_FILE, EXCEL_SETTINGS_FILE, EXCEL_BACKTESTING_FILE
from src.core.logger import setup_logging

logger = setup_logging()

def initialize_excel_files():
    """Crea los archivos Excel si no existen."""
    files = [EXCEL_SIGNALS_FILE, EXCEL_SETTINGS_FILE, EXCEL_BACKTESTING_FILE]
    for file in files:
        if not os.path.exists(file):
            df = pd.DataFrame()
            # Crear directorio si no existe
            os.makedirs(os.path.dirname(file), exist_ok=True)
            df.to_excel(file, index=False)
            logger.info(f"Archivo Excel creado: {file}")

def save_signal_to_excel(signal_data):
    """Guarda una nueva señal en el archivo Excel."""
    try:
        if os.path.exists(EXCEL_SIGNALS_FILE):
            df = pd.read_excel(EXCEL_SIGNALS_FILE)
        else:
            df = pd.DataFrame()

        new_row = pd.DataFrame([signal_data])
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_excel(EXCEL_SIGNALS_FILE, index=False)
        logger.info(f"Señal guardada en Excel: {signal_data['asset']}")
    except Exception as e:
        logger.error(f"Error al guardar señal en Excel: {e}")

def update_signal_in_excel(asset, status, pnl=None):
    """Actualiza el estado de una señal en el archivo Excel."""
    try:
        if not os.path.exists(EXCEL_SIGNALS_FILE):
            return

        df = pd.read_excel(EXCEL_SIGNALS_FILE)
        # Buscar la última señal activa para ese activo
        mask = (df['asset'] == asset) & (df['status'] == 'ACTIVE')
        if mask.any():
            idx = df[mask].index[-1]
            df.at[idx, 'status'] = status
            if pnl is not None:
                df.at[idx, 'pnl'] = pnl
            df.to_excel(EXCEL_SIGNALS_FILE, index=False)
            logger.info(f"Señal de {asset} actualizada en Excel a {status}")
    except Exception as e:
        logger.error(f"Error al actualizar señal en Excel: {e}")

def is_asset_active_in_excel(asset):
    """Verifica si un activo ya tiene una señal activa en Excel."""
    try:
        if not os.path.exists(EXCEL_SIGNALS_FILE):
            return False

        df = pd.read_excel(EXCEL_SIGNALS_FILE)
        if df.empty:
            return False
            
        active_signals = df[(df['asset'] == asset) & (df['status'] == 'ACTIVE')]
        return not active_signals.empty
    except Exception as e:
        logger.error(f"Error al verificar activo en Excel: {e}")
        return False

def load_settings_from_excel():
    """Carga la configuración desde el archivo Excel."""
    try:
        if os.path.exists(EXCEL_SETTINGS_FILE):
            return pd.read_excel(EXCEL_SETTINGS_FILE).to_dict(orient='records')
        return []
    except Exception as e:
        logger.error(f"Error al cargar configuración desde Excel: {e}")
        return []

