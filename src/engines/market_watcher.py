
import asyncio
import MetaTrader5 as mt5
from src.core.logger import setup_logging
from src.core.mt5_utils import initialize_mt5, shutdown_mt5, get_ohlc_data, is_position_open, get_position_pnl
from src.engines.signal_engine import evaluate_signal
from src.core.data_models import Signal
from src.managers.telegram_manager import send_signal_notification, send_telegram_message
from src.core.database import insert_signal, update_signal_status, get_active_signals
from src.managers.excel_manager import save_signal_to_excel, is_asset_active_in_excel, update_signal_in_excel
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
                        # 1. Verificar si hay una señal activa en el sistema (Excel/BD)
                        if is_asset_active_in_excel(asset):
                            # Verificar si la posición sigue abierta en MetaTrader5
                            if not is_position_open(asset):
                                logger.info(f"La posición para {asset} se ha cerrado en MT5. Actualizando registros...")
                                
                                # Obtener el último PnL (opcional, si se puede recuperar del historial)
                                # Por ahora marcamos como CLOSED
                                update_signal_in_excel(asset, "CLOSED")
                                
                                # También actualizar en la base de datos
                                active_signals = get_active_signals()
                                for s in active_signals:
                                    if s.asset == asset:
                                        # Aquí necesitaríamos el ID de la señal, pero por ahora simplificamos
                                        # update_signal_status(s.id, "CLOSED")
                                        pass
                                
                                await send_telegram_message(f"✅ *Operación Cerrada:* {asset}. El bot reanudará la búsqueda de señales para este activo.")
                            else:
                                logger.debug(f"Posición para {asset} sigue abierta. Saltando búsqueda.")
                                continue

                        # 2. Si no hay posición activa, proceder con la búsqueda de señales
                        # Obtener timeframes configurados
                        tf_signal = config["timeframe_signal"][0]
                        tf_trend = config["timeframe_trend"][-1]
                        
                        df_signal = get_ohlc_data(asset, tf_signal, 300)
                        df_trend = get_ohlc_data(asset, tf_trend, 300)
                        
                        if df_signal is not None and df_trend is not None:
                            signal = evaluate_signal(asset, df_signal, df_trend)
                            
                            if signal:
                                logger.info(f"¡NUEVA SEÑAL DETECTADA! {asset} {signal.type}")
                                
                                # Notificar y Guardar
                                await send_signal_notification(signal)
                                insert_signal(signal)
                                save_signal_to_excel(signal.dict())
                                
                                logger.info(f"Señal para {asset} procesada y enviada.")
                    
                    except Exception as e:
                        logger.error(f"Error procesando {asset}: {str(e)}")

            await asyncio.sleep(MONITORING_INTERVAL_SECONDS)
    
    except asyncio.CancelledError:
        logger.info("Monitoreo de mercado cancelado.")
    finally:
        shutdown_mt5()

