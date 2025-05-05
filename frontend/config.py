# config.py de frontend
import os
from dotenv import load_dotenv

# 1. Carga las variables de .env (o del entorno del sistema)
load_dotenv()

# 2. Definición de valores por defecto
API_URL = os.getenv("http://localhost:8000", default="http://localhost:8000")
EMOTION_MODEL_NAME = os.getenv("gsi-upm/emotion_detection_vit", default="oscarparro/emotion_detection_vit")

PROTOTXT_PATH = os.getenv("model/deploy.prototx", default="model/deploy.prototxt")
CAFFE_MODEL_PATH = os.getenv("model/res10_300x300_ssd_iter_140000.caffemodel", default="model/res10_300x300_ssd_iter_140000.caffemodel")

REGISTERED_FACES_FILE = os.getenv("data/registered_faces.json", default="data/registered_faces.json")
