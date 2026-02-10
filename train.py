# train.py
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

# Dataset de ejemplo (simula Titanic)
# columnas: [edad, clase, sexo]
# clase: 1=first,2=second,3=third
# sexo: 0=male,1=female
X = np.array([
    [22, 3, 0],
    [38, 1, 1],
    [26, 3, 1],
    [35, 1, 1],
    [35, 3, 0],
    [54, 1, 0],
    [2,  3, 1],
    [27, 2, 0],
])

# 1=sobrevivió, 0=no sobrevivió
y = np.array([0, 1, 1, 1, 0, 0, 1, 0])

model = LogisticRegression()
model.fit(X, y)

# Guardar modelo
with open("titanic_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Modelo entrenado y guardado como titanic_model.pkl")
