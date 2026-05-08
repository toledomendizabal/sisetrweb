
import sys
import os

# Añadir el directorio raíz al path para poder importar los módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.mt5_utils import initialize_mt5, shutdown_mt5
from src.managers.telegram_manager import send_telegram_message
import asyncio

async def run_diagnostics():
    print("--- Iniciando Diagnóstico de SISETRWEB ---")
    
    # 1. Verificar Python
    print(f"Python Version: {sys.version}")
    
    # 2. Verificar MT5
    print("\nVerificando conexión con MetaTrader 5...")
    if initialize_mt5():
        print("✅ Conexión con MT5 exitosa.")
        shutdown_mt5()
    else:
        print("❌ Error al conectar con MT5. Asegúrate de que la terminal esté abierta.")

    # 3. Verificar Telegram (Opcional)
    print("\n¿Deseas enviar un mensaje de prueba a Telegram? (s/n)")
    # En un script automatizado esto se saltaría o usaría una variable de entorno
    # choice = input().lower()
    choice = 'n' # Por defecto no para el diagnóstico automático
    if choice == 's':
        await send_telegram_message("Prueba de diagnóstico de SISETRWEB")
        print("✅ Mensaje de prueba enviado.")

    print("\n--- Diagnóstico Completado ---")

if __name__ == "__main__":
    asyncio.run(run_diagnostics())
