# 🥑 Urban Grocers API Testing Automation 

**Autor**: Yostin Chavarría Castro

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pytest](https://img.shields.io/badge/Pytest-Framework-green)
![Requests](https://img.shields.io/badge/Requests-Library-orange)

## 📌 Descripción  

Este proyecto contiene **pruebas automatizadas** para la API de **Urban Grocers**.  
El objetivo es validar los endpoints principales de la API mediante el uso de **Pytest** y la librería **Requests**, asegurando que las operaciones de creación de usuarios y kits funcionen correctamente.  

---

## 🔍 Endpoints probados  

| Método | Endpoint       | Descripción |
|--------|----------------|-------------|
| `POST` | `/users`       | Crear un nuevo usuario |
| `POST` | `/kits`        | Crear un kit para el usuario |
| `GET`  | `/kits/{id}`   | Consultar si el kit fue creado |

---

## 📂 Estructura del proyecto 

    ```bash
    urban-grocers/
    ├── configuration.py              # Configuración necesaria para las pruebas (host, urls, etc.)
    ├── data.py                       # Datos de prueba utilizados en las requests
    ├── sender_stand_request.py       # Funciones para interactuar con la API (POST, GET, manejo de respuestas)
    └── create_kit_name_kit_test.py   # Archivo con las pruebas automatizadas y sus assert

## ⚙️ Requisitos  

- Python **3.8** o superior  
- Entorno virtual recomendado  
- Librerías:  
  - `pytest`  
  - `requests`  


## 🚀 Instalación y ejecución

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/urban-grocers.git
   cd urban-grocers

2. Crear un entorno virtual:

   ```bash
   python -m venv venv

3. Activar el entorno virtual:
   
   ```bash
   # En Windows:
   venv\Scripts\activate

   # En macOS/Linux:
   source venv/bin/activate

5. Instalar las dependencias necesarias:

   ```bash
   pip install requests pytest

6. Ejecutar las pruebas:

    ```bash
   pytest -v
