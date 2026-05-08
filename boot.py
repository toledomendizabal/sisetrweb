#!/usr/bin/env python3
"""
SISETRWEB - Script de Inicio Principal
Ejecuta el bot SISETRWEB correctamente desde la carpeta raíz
Uso: python boot.py
"""

import sys
import os
import asyncio
from pathlib import Path

# Obtener la carpeta raíz del proyecto
ROOT_DIR = Path(__file__).parent.absolute()

# Agregar la carpeta raíz al path de Python
sys.path.insert(0, str(ROOT_DIR))

# Importar y ejecutar el main
if __name__ == '__main__':
    try:
        # Cambiar al directorio raíz
        os.chdir(ROOT_DIR)
        
        # Importar el módulo principal
        from src.main import main
        
        # Ejecutar el bot (main es una corrutina asíncrona, necesita asyncio.run)
        asyncio.run(main())
    except ImportError as e:
        print(f"Error de importación: {e}")
        print("\nAsegúrate de que estás en la carpeta correcta:")
        print(f"  cd {ROOT_DIR}")
        print("\nY que el entorno virtual está activado:")
        print("  .\\venv\\Scripts\\activate")
        sys.exit(1)
    except Exception as e:
        print(f"Error al iniciar el bot: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
