import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

# 1. Generar dataset estático
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# 2. Entrenar modelo de Machine Learning
model = LinearRegression()
model.fit(X, y)

# 3. Guardar modelo entrenado
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Modelo entrenado y guardado como model.pkl")
