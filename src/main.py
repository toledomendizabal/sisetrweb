# src/main.py

import asyncio
import uvicorn
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from .core.logger import setup_logging
from .api.main import app as fastapi_app
from .engines.market_watcher import start_market_watcher
from .managers.telegram_manager import send_daily_test_message
from .managers.email_manager import send_daily_report
from .engines.backtesting_engine import run_daily_backtesting
from config.settings import TELEGRAM_DAILY_MESSAGE_TIME, DAILY_REPORT_TIME

logger = setup_logging()

async def start_fastapi():
    config = uvicorn.Config(fastapi_app, host="0.0.0.0", port=8000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

async def main():
    logger.info("Iniciando SISETRWEB Bot...")

    # Inicializar el scheduler
    scheduler = AsyncIOScheduler()

    # Programar tareas diarias
    scheduler.add_job(send_daily_test_message, 'cron', hour=int(TELEGRAM_DAILY_MESSAGE_TIME.split(':')[0]), minute=int(TELEGRAM_DAILY_MESSAGE_TIME.split(':')[1]))
    scheduler.add_job(run_daily_backtesting, 'cron', hour=int(DAILY_REPORT_TIME.split(':')[0]), minute=int(DAILY_REPORT_TIME.split(':')[1]))
    scheduler.add_job(send_daily_report, 'cron', hour=int(DAILY_REPORT_TIME.split(':')[0]), minute=int(DAILY_REPORT_TIME.split(':')[1]))

    scheduler.start()
    logger.info("Scheduler iniciado.")

    # Iniciar el Market Watcher en un hilo separado o tarea asíncrona
    asyncio.create_task(start_market_watcher())
    logger.info("Market Watcher iniciado.")

    # Iniciar el servidor FastAPI
    await start_fastapi()

if __name__ == "__main__":
    asyncio.run(main())
