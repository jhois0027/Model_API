from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()

# Cargar modelo correcto
with open("titanic_model.pkl", "rb") as f:
    model = pickle.load(f)

# Esquema del JSON
class Persona(BaseModel):
    edad: int
    clase: str
    sexo: str

@app.get("/test")
def test():
    return {"status": "API Titanic funcionando"}

@app.post("/predict")
def predict(data: Persona):

    # Mapear texto a números
    clase_map = {"first": 1, "second": 2, "third": 3}
    sexo_map = {"male": 0, "female": 1}

    clase = clase_map.get(data.clase.lower())
    sexo = sexo_map.get(data.sexo.lower())

    if clase is None or sexo is None:
        return {"error": "Clase o sexo inválido"}

    X = np.array([[data.edad, clase, sexo]])

    pred = model.predict(X)[0]

    resultado = "Sobrevivió" if pred == 1 else "No sobrevivió"

    return {
        "edad": data.edad,
        "clase": data.clase,
        "sexo": data.sexo,
        "resultado": resultado
    }
