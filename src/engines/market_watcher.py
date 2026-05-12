
import asyncio
import MetaTrader5 as mt5
from src.core.logger import setup_logging
from src.core.mt5_utils import initialize_mt5, shutdown_mt5, get_ohlc_data
from src.engines.signal_engine import evaluate_signal
from src.core.data_models import Signal
from src.managers.telegram_manager import send_signal_notification
from src.core.database import insert_signal
from src.managers.excel_manager import save_signal_to_excel, is_asset_active_in_excel
from config.settings import ASSETS_CONFIG, MONITORING_INTERVAL_SECONDS

logger = setup_logging()

async def start_market_watcher():
    if not initialize_mt5():
        logger.error("No se pudo inicializar MetaTrader5. El monitoreo de mercado no se iniciará.")
        return

    logger.info("Iniciando bucle de monitoreo de mercado...")
    
    try:
        while True:
            for asset, config in ASSETS_CONFIG.items():
                if config["enabled"]:
                    try:
                        # Obtener timeframes configurados
                        tf_signal = config["timeframe_signal"][0] # Usamos el primero por defecto para la señal
                        tf_trend = config["timeframe_trend"][-1]  # Usamos el último (más alto) para la tendencia
                        
                        # Obtener datos OHLC (necesitamos suficientes para los indicadores, ej: 300 velas)
                        df_signal = get_ohlc_data(asset, tf_signal, 300)
                        df_trend = get_ohlc_data(asset, tf_trend, 300)
                        
                        if df_signal is not None and df_trend is not None:
                            # Evaluar si hay una señal
                            signal = evaluate_signal(asset, df_signal, df_trend)
                            
                            if signal:
                                # Evitar duplicados si ya hay una señal activa para este activo
                                if not is_asset_active_in_excel(asset):
                                    logger.info(f"¡NUEVA SEÑAL DETECTADA! {asset} {signal.type}")
                                    
                                    # 1. Notificar por Telegram
                                    await send_signal_notification(signal)
                                    
                                    # 2. Guardar en Base de Datos
                                    insert_signal(signal)
                                    
                                    # 3. Guardar en Excel
                                    save_signal_to_excel(signal.dict())
                                    
                                    logger.info(f"Señal para {asset} procesada y enviada.")
                                else:
                                    logger.debug(f"Señal detectada para {asset} pero ya existe una activa.")
                    
                    except Exception as e:
                        logger.error(f"Error procesando {asset}: {str(e)}")

            await asyncio.sleep(MONITORING_INTERVAL_SECONDS)
    
    except asyncio.CancelledError:
        logger.info("Monitoreo de mercado cancelado.")
    finally:
        shutdown_mt5()

