# Imagen base oficial de Python
FROM python:3.11-slim

# Variables de entorno para evitar buffering
ENV PYTHONUNBUFFERED=1

# Crear directorio de trabajo
WORKDIR /app

# Copiar requirements y luego instalarlos (optimiza cache de Docker)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Exponer puerto 5000 para la API
EXPOSE 5000

# Comando para iniciar la API
CMD ["python", "app.py"]
