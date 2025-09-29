import requests
import pandas as pd
import numpy as np

# --- Configuración ---
url = "http://127.0.0.1:5000/predict"
num_tests = 10  # Número de pruebas

# --- Cargar datos de test ---
X_test = pd.read_csv("X_test.csv")

# Reemplazar NaN por 0 (o podrías usar otra estrategia)
X_test = X_test.fillna(0)

# Tomar las primeras 10 filas
features_list = X_test.iloc[:num_tests].values.tolist()

# --- Probar API ---
for i, features in enumerate(features_list):
    data_json = {"features": features}
    try:
        response = requests.post(url, json=data_json)
        result = response.json()
        pred = result.get("prediction", [None])[0]
        label = "Maligno" if pred == 1 else "Benigno"
        print(f"Prueba {i+1}: {label}")
    except Exception as e:
        print(f"Error en prueba {i+1}: {e}")
