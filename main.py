from fastapi import FastAPI
import pickle

app = FastAPI()

# Cargar el modelo entrenado
with open("model.pkl", "rb") as archivo:
    modelo = pickle.load(archivo)

@app.get("/")
def home():
    return {"mensaje": "API financiera funcionando correctamente"}

@app.get("/predict")
def predict(
    salario: float,
    arriendo: float,
    servicios: float,
    transporte: float,
    mercado: float,
    otros: float
):
    # Predicción del gasto total
    prediccion = modelo.predict([[arriendo, servicios, transporte, mercado, otros]])
    gasto_total = round(float(prediccion[0]), 2)

    # Dinero restante
    restante = round(salario - gasto_total, 2)

    # Formato COP
    salario_fmt = f"${salario:,.2f} COP"
    gasto_fmt = f"${gasto_total:,.2f} COP"
    restante_fmt = f"${restante:,.2f} COP"

    if restante >= 0:
        estado = "La persona tiene capacidad de ahorro."
    else:
        estado = "La persona está en déficit financiero."

    mensaje = (
        f"La persona gana mensualmente {salario_fmt}. "
        f"Según sus gastos, el total estimado es {gasto_fmt}. "
        f"Le quedan disponibles {restante_fmt}. {estado}"
    )

    print(mensaje)

    return {
        "salario_mensual": salario_fmt,
        "gasto_total_estimado": gasto_fmt,
        "dinero_restante": restante_fmt,
        "estado_financiero": estado,
        "mensaje": mensaje
    }
