from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI(title="Model API")

# Cargar modelo entrenado
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def home():
    return {"mensaje": "API funcionando correctamente"}

@app.get("/test")
def test():
    return {"status": "ok"}

@app.post("/predict")
def predict(value: float):
    prediction = model.predict(np.array([[value]]))
    return {"prediction": prediction[0]}
