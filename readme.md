# 💰 finanzas_API

Una API en Python para estimar gastos mensuales y cálculo de saldo disponible según ingresos y gastos.  
Construida con **FastAPI**, entrenada con **Scikit-Learn** y empaquetada en **Docker**.  

---

## 🚀 Tecnologías

- Python 3.9+  
- FastAPI  
- Scikit-Learn  
- Pandas & NumPy  
- Docker  
- Vagrant (para entorno Linux reproducible)  

---

## 🛠️ Instalación y ejecución

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/jhois0027/finanzas_API.git

cd finanzas_API

2️⃣ Usando Vagrant (Linux VM)
vagrant up
vagrant ssh
cd /vagrant/finanzas_API

3️⃣ Construir y correr Docker
# Construir imagen
docker build -t finanzas_api:1.0 .

# Correr API
docker run -p 8000:8000 finanzas_api:1.0
Abre tu navegador en: http://localhost:8000/docs

🧮 Uso de la API
Endpoint principal
POST /predict

Body JSON:

{
  "ingresos": 2000000
  "arriendo": 450000,
  "servicios": 130000,
  "transporte": 262500,
  "mercado": 700000,
  "otros": 150000,
  
}

Respuesta
{
  "salario_mensual": "$2,000,000.00 COP",
  "gasto_total_estimado": "$1,697,023.25 COP",
  "dinero_restante": "$302,976.75 COP",
  "estado_financiero": "La persona tiene capacidad de ahorro.",

  "mensaje": "La persona gana mensualmente $2,000,000.00 COP. Según sus gastos, el total estimado es $1,697,023.25 COP. Le quedan disponibles $302,976.75 COP. La persona tiene capacidad de ahorro."
}

📂 Estructura del proyecto
VAGRANT_API/
├─ .vagrant/
│  └─ machines/rgloader
├─ finanzas_API/
│  ├─ __pycache__/
│  ├─ .pytest_cache/
│  ├─ test/
│  ├─ .gitignore
│  ├─ dataset_estatico.csv
│  ├─ Dockerfile
│  ├─ main.py
│  ├─ model.pkl
│  ├─ readme.md
│  ├─ requirements.txt
│  └─ train.py
├─ ubuntu-bionic-18.04-cloudimg-console.log
└─ Vagrantfile

✨ Autor
Jhois0027

GitHub: https://github.com/jhois0027


📝 Notas
El dataset es estático y generado aleatoriamente para fines de demostración.

La API puede integrarse con cualquier frontend o app para estimar gastos en tiempo real.