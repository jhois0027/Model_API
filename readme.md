# 🚀 Virtualización y APIs de Machine Learning

Este proyecto documenta el proceso de despliegue de una API de predicción utilizando **FastAPI**, **Docker** y **Vagrant**, cumpliendo con los requerimientos de virtualización y contenedorización.

## 🛠️ 1. Infraestructura y Virtualización (Vagrant & Linux)
El entorno de desarrollo se configuró sobre una máquina virtual para garantizar aislamiento:
* **Entorno:** Ubuntu 18.04 LTS (Bionic) gestionado con Vagrant.
* **Preparación:** Actualización de paquetes del sistema y gestión de permisos:
  ```bash
  sudo apt-get update && sudo apt-get upgrade -y

  🧠 2. Modelo de Machine Learning (train.py)
Se implementó un script de entrenamiento que realiza lo siguiente:

Dataset: Generación de un conjunto de datos estático para el entrenamiento.

Entrenamiento: Creación de un modelo de Machine Learning (ej. Regresión o Clasificación).

Persistencia: Exportación del modelo entrenado al archivo .model.pkl

⚡ 3. FastAPI funcional (main.py)
La API se construyó con FastAPI incluyendo los siguientes endpoints:

GET /: Endpoint de prueba para verificar el estado de la API.

POST /predict: Recibe peticiones con datos y retorna la predicción usando el archivo ..pkl

🧪 4. Pruebas Unitarias (test/test_main.py)
Se desarrollaron pruebas para validar la funcionalidad de los endpoints utilizando , asegurando que la API responda correctamente a las peticiones GET y POST.pytest

🐳 5. Contenedorización (Dockerfile)
El fue configurado siguiendo los estándares solicitados:Dockerfile

Instalación de dependencias: Basado en .requirements.txt

Configuración del entorno: Definición de variables necesarias para la ejecución.

Ejecución de pruebas: Comando para validar los tests antes del despliegue.

Levantamiento: Comando automático para iniciar el servidor Uvicorn.

Comandos Docker
Construir imagen: docker build -t model_api:1.0 .

Ejecutar localmente: docker run -p 8000:8000 ingrij27/model_api:1.0

🌐 6. Publicación en Docker Hub
La imagen final ha sido etiquetada y publicada exitosamente:

Usuario: ingrij27

Repositorio: model_api

Versión/Tag: 1.0

Comando de descarga: docker pull ingrij27/model_api:1.0