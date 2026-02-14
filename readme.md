**💰 finanzas_API 🚀**

Una API en Python para estimar gastos mensuales y calcular el saldo disponible según ingresos y gastos.
Construida con FastAPI, entrenada con Scikit-Learn y empaquetada en Docker, con entorno reproducible usando Vagrant.

**🛠️ Tecnologías**

Python 3.9+

FastAPI

Scikit-Learn

Pandas & NumPy

Docker

Vagrant (para entorno Linux reproducible)

VAGRANT_API/
├─ 📁 .vagrant/
│  └─ 📁 machines/
│      └─ 📄 rgloader
├─ 📁 finanzas_API/
│  ├─ 📁 __pycache__/
│  ├─ 📁 .pytest_cache/
│  ├─ 📁 test/
│  ├─ 📄 .gitignore
│  ├─ 📄 dataset_estatico.csv
│  ├─ 📄 Dockerfile
│  ├─ 📄 main.py
│  ├─ 📄 model.pkl
│  ├─ 📄 readme.md
│  ├─ 📄 requirements.txt
│  └─ 📄 train.py
├─ 📄 ubuntu-bionic-18.04-cloudimg-console.log
└─ 📄 Vagrantfile


**🚀 Instalación y ejecución**
1️⃣ Clonar el repositorio
git clone https://github.com/jhois0027/finanzas_API.git
cd finanzas_API

2️⃣ Levantar la máquina virtual con Vagrant
vagrant up
vagrant ssh
cd /vagrant/finanzas_API

3️⃣ Construir y ejecutar la API con Docker
# Construir imagen
docker build -t finanzas_api:1.0 .

# Ejecutar contenedor
docker run -p 8000:8000 finanzas_api:1.0


Abre tu navegador en: http://localhost:8000/docs

**🧮 Uso de la API**
Endpoint principal: POST /predict

Body JSON ejemplo:

{
  "ingresos": 2000000,
  "arriendo": 450000,
  "servicios": 130000,
  "transporte": 262500,
  "mercado": 700000,
  "otros": 150000
}


Respuesta de ejemplo:

{
  "salario_mensual": "$2,000,000.00 COP",
  "gasto_total_estimado": "$1,697,023.25 COP",
  "dinero_restante": "$302,976.75 COP",
  "estado_financiero": "La persona tiene capacidad de ahorro.",
  "mensaje": "La persona gana mensualmente $2,000,000.00 COP. Según sus gastos, el total estimado es $1,697,023.25 COP. Le quedan disponibles $302,976.75 COP. La persona tiene capacidad de ahorro."
}

**🧠 Entrenamiento del modelo (train.py)**

**Dataset:** dataset_estatico.csv (generado aleatoriamente para demostración)

**Modelo:** Clasificación/regresión con Scikit-Learn

**Persistencia:** model.pkl

🧪 Pruebas Unitarias (test/test_main.py)

Validan que los endpoints GET y POST funcionen correctamente

**Ejecutar con:**

pytest

🐳 Contenedorización (Docker)

**Imagen:** finanzas_api:1.0

**Construcción:**

docker build -t finanzas_api:1.0 .


**Ejecución local:**

docker run -p 8000:8000 finanzas_api:1.0


**Posible publicación en Docker Hub:**

docker tag finanzas_api:1.0 usuario/finanzas_api:1.0
docker push usuario/finanzas_api:1.0

✨ Autor

Jhois0027
GitHub: https://github.com/jhois0027

**📝 Notas**

La API es demostrativa y puede integrarse con cualquier frontend para estimar gastos en tiempo real.

Vagrant asegura un entorno controlado y reproducible.


Docker facilita la portabilidad y despliegue de la API.
