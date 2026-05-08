
import asyncio
import MetaTrader5 as mt5
from src.core.logger import setup_logging
from src.core.mt5_utils import initialize_mt5, shutdown_mt5, get_ohlc_data
from config.settings import ASSETS_CONFIG, MONITORING_INTERVAL_SECONDS

logger = setup_logging()

async def start_market_watcher():
    if not initialize_mt5():
        logger.error("No se pudo inicializar MetaTrader5. El monitoreo de mercado no se iniciará.")
        return

    while True:
        for asset, config in ASSETS_CONFIG.items():
            if config["enabled"]:
                # Aquí se obtendrían los datos más recientes para el análisis
                # Por ahora, solo logueamos que se está monitoreando
                logger.info(f"Monitoreando {asset}...")
                # Ejemplo de cómo obtener datos (se necesitaría un timeframe específico)
                # data = get_ohlc_data(asset, "1M", 1) # Obtener la última vela de 1 minuto
                # if data is not None and not data.empty:
                #     latest_price = data["close"].iloc[-1]
                #     logger.info(f"Último precio de {asset}: {latest_price}")

        await asyncio.sleep(MONITORING_INTERVAL_SECONDS)

    shutdown_mt5()

