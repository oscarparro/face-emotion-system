# config.py de frontend
import os
from dotenv import load_dotenv

# 1. Carga las variables de .env (o del entorno del sistema)
load_dotenv()

# 2. Definición de valores por defecto
API_URL = os.getenv("API_URL", "http://localhost:8000")