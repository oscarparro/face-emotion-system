# config.py
import os
from dotenv import load_dotenv

# 1. Carga las variables de .env (o del entorno del sistema)
load_dotenv()

# 2. Definición de valores por defecto
EMOTION_MODEL_NAME = os.getenv("gsi-upm/emotion_detection_vit", "oscarparro/emotion_detection_vit")
