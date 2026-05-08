
import asyncio
from telegram import Bot
from config.settings import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
from src.core.logger import setup_logging

logger = setup_logging()

async def send_telegram_message(message):
    """Envía un mensaje a través del bot de Telegram."""
    try:
        bot = Bot(token=TELEGRAM_BOT_TOKEN)
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message, parse_mode='Markdown')
        logger.info("Mensaje de Telegram enviado correctamente.")
    except Exception as e:
        logger.error(f"Error al enviar mensaje de Telegram: {e}")

async def send_signal_notification(signal):
    """Envía una notificación de nueva señal a Telegram."""
    message = (
        f"🚀 *NUEVA SEÑAL DETECTADA*\n\n"
        f"*Activo:* {signal.asset}\n"
        f"*Tipo:* {signal.type}\n"
        f"*Entrada:* {signal.entry_price:.5f}\n"
        f"*Stop Loss:* {signal.stop_loss:.5f} ({signal.sl_distance_pips:.1f} pips)\n"
        f"*TP1 (1:3):* {signal.tp1:.5f}\n"
        f"*TP2 (1:6):* {signal.tp2:.5f}\n"
        f"*TP3 (1:10):* {signal.tp3:.5f}\n"
        f"*Lotaje:* {signal.lot_size}\n"
        f"*Score:* {signal.score}\n"
        f"*Timeframe:* {signal.timeframe}\n"
        f"*Indicadores:* {', '.join(signal.indicators_met)}"
    )
    await send_telegram_message(message)

async def send_daily_test_message():
    """Envía el mensaje de prueba diario a las 9:00 AM."""
    message = "✅ *SISETRWEB Bot:* Sistema operativo y monitoreando mercados. (Mensaje de prueba diario 9:00 AM)"
    await send_telegram_message(message)

