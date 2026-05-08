
import logging
import os
from config.settings import LOGS_DIR, SYSTEM_LOG_FILE, SIGNALS_LOG_FILE, MONITORING_LOG_FILE, BACKTESTING_LOG_FILE

def setup_logging():
    """Configura el sistema de logging para el bot."""
    if not os.path.exists(LOGS_DIR):
        os.makedirs(LOGS_DIR)

    # Configuración del logger principal
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(SYSTEM_LOG_FILE),
            logging.StreamHandler()
        ]
    )
    logger = logging.getLogger(__name__)

    # Logger para señales
    signals_logger = logging.getLogger("signals")
    signals_logger.setLevel(logging.INFO)
    signals_handler = logging.FileHandler(SIGNALS_LOG_FILE)
    signals_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    signals_logger.addHandler(signals_handler)
    signals_logger.propagate = False # Evitar que los logs se dupliquen en el logger principal

    # Logger para monitoreo
    monitoring_logger = logging.getLogger("monitoring")
    monitoring_logger.setLevel(logging.INFO)
    monitoring_handler = logging.FileHandler(MONITORING_LOG_FILE)
    monitoring_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    monitoring_logger.addHandler(monitoring_handler)
    monitoring_logger.propagate = False

    # Logger para backtesting
    backtesting_logger = logging.getLogger("backtesting")
    backtesting_logger.setLevel(logging.INFO)
    backtesting_handler = logging.FileHandler(BACKTESTING_LOG_FILE)
    backtesting_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    backtesting_logger.addHandler(backtesting_handler)
    backtesting_logger.propagate = False

    return logger

