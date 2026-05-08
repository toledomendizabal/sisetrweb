
from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import asyncio
import json
from datetime import datetime
from src.core.database import get_active_signals
from config.settings import ASSETS_CONFIG, CAPITAL_BASE

app = FastAPI(title="SISETRWEB Dashboard")

# Configuración de templates (si se usara Jinja2)
# templates = Jinja2Templates(directory="src/api/templates")

@app.get("/")
async def get_dashboard():
    return {"message": "SISETRWEB API is running. Access /docs for API documentation."}

@app.get("/status")
async def get_status():
    return {
        "status": "online",
        "timestamp": datetime.now().isoformat(),
        "active_assets": [a for a, c in ASSETS_CONFIG.items() if c["enabled"]],
        "capital_base": CAPITAL_BASE
    }

@app.get("/signals/active")
async def get_signals():
    return get_active_signals()

@app.websocket("/ws/market-data")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # Enviar datos de mercado en tiempo real simulados o reales
            data = {
                "timestamp": datetime.now().isoformat(),
                "prices": {"EURUSD": 1.0850, "XAUUSD": 2350.20} # Ejemplo
            }
            await websocket.send_text(json.dumps(data))
            await asyncio.sleep(10)
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        await websocket.close()

