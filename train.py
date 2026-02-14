import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

np.random.seed(42)

# Generar dataset estático con gastos reales
data = {
    "arriendo": np.random.randint(300000, 800000, 100),
    "servicios": np.random.randint(80000, 200000, 100),
    "transporte": np.random.randint(150000, 400000, 100),
    "mercado": np.random.randint(400000, 900000, 100),
    "otros": np.random.randint(100000, 300000, 100),
}

df = pd.DataFrame(data)

# Variable objetivo: gasto total mensual
df["gasto_total"] = (
    df["arriendo"]
    + df["servicios"]
    + df["transporte"]
    + df["mercado"]
    + df["otros"]
    + np.random.normal(0, 50000, 100)  # pequeño ruido
)

df.to_csv("dataset_estatico.csv", index=False)

print("Dataset generado correctamente.")

X = df[["arriendo", "servicios", "transporte", "mercado", "otros"]]
y = df["gasto_total"]

modelo = LinearRegression()
modelo.fit(X, y)

print("Modelo entrenado correctamente.")

with open("model.pkl", "wb") as archivo:
    pickle.dump(modelo, archivo)

print("Modelo guardado como model.pkl")
