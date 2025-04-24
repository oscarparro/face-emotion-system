FROM python:3.11-slim

# 1. Crear directorio de trabajo
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      build-essential \
      cmake \
      libgtk2.0-dev \
      libgl1 \
      libglib2.0-0 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY streamlit-app.py config.py /app/
COPY model/ ./model/

# 4. Crear carpeta data para el JSON
RUN mkdir -p /app/data

# Variable que usará la app para saber dónde está el backend

EXPOSE 8501
CMD ["streamlit", "run", "streamlit-app.py", "--server.address=0.0.0.0"]
