"""
SISETRWEB - Punto de entrada principal del bot
Este archivo permite ejecutar el módulo como: python -m src
"""

import sys
import os

# Agregar la carpeta raíz al path para que Python encuentre los módulos
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importar y ejecutar el main
from src.main import main

if __name__ == '__main__':
    main()
