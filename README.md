# Breast Cancer Prediction API

Este proyecto entrena un modelo de Machine Learning para predecir cáncer de mama y lo expone mediante una API en Flask.

## 🚀 Características
- Entrenamiento y guardado del modelo (`.pkl`).
- API con Flask con endpoints:
  - GET `/` → Estado del servicio
  - POST `/predict` → Predicción
- Dockerización para despliegue sencillo
- CI/CD con GitHub Actions (build, test y push a Docker Hub)

## 📂 Estructura
- app.py → API
- train_model.py → Entrenamiento del modelo
- breast_cancer_model.pkl → Modelo entrenado
- Dockerfile → Imagen Docker
- requirements.txt → Dependencias
- test_api.py → Tests básicos

## 🔧 Instalación
```bash
git clone https://github.com/Leandroaraya/Act_Mod10.git
cd breast-cancer-api
pip install -r requirements.txt
python app.py
