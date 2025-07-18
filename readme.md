# Weather API - FastAPI on AWS Lambda

Este proyecto es una API REST construida con **FastAPI** que permite consultar el clima actual de una ciudad utilizando un servicio externo (como OpenWeatherMap) y almacenar las búsquedas en una base de datos PostgreSQL alojada en **AWS RDS**. La API está diseñada para ejecutarse como función **AWS Lambda** mediante AWS API Gateway.

## Características

- ✅ Obtener el clima actual de cualquier ciudad.
- 📜 Guardar y consultar el historial de búsquedas.
- ☁️ Integración con una API externa de clima.
- 🐍 Backend en FastAPI.
- ☁️ Despliegue en AWS Lambda con base de datos en RDS PostgreSQL.

---

## Endpoints

### `GET /weather?city={city}`

Obtiene la información del clima actual para la ciudad especificada.

- **Parámetros**:  
  - `city` (string, requerido): Nombre de la ciudad a consultar.
- **Respuesta**:
  ```json
  {
            "id": "query-38dbeeed-6461-483c-bee7-2b7a7c98cde7",
            "country": "Argentina",
            "region": "Distrito Federal",
            "temp_c": "4.3",
            "humidity": "100",
            "city": "Buenos Aires",
            "source_query": "127.0.0.1",
            "dateQuery": "2025-07-18",
            "condition": "Clear",
            "wind_kph": "6.5"
    },

### `GET /history`

Obtiene el historial global de consultas.

- **Respuesta**:
  ```json
  [{
            "id": "query-38dbeeed-6461-483c-bee7-2b7a7c98cde7",
            "country": "Argentina",
            "region": "Distrito Federal",
            "temp_c": "4.3",
            "humidity": "100",
            "city": "Buenos Aires",
            "source_query": "127.0.0.1",
            "dateQuery": "2025-07-18",
            "condition": "Clear",
            "wind_kph": "6.5"
    },]

### `POST /weather?city={city}`

Obtiene la información del clima actual para la ciudad especificada.

- **Parámetros**:  
  - `city` (string, requerido): Nombre de la ciudad a consultar.
- **Respuesta**:
  ```json
  {
    "status": 200,
    "message": "Registro de la ciudad Buenos aires creado con exito"
    }

## Configuración

Variables de entorno requeridas

- **Variables de entorno requeridas**:  
    - `WEATHER_API_KEY`
    - `POSTGRES_PASSWORD`
    - `POSTGRES_USER`
    - `PORT_DB`
    - `HOST_DB`

## Instalación local

```bash
git clone https://github.com/G9Mares/clima_back.git
cd weather-fastapi
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
pip install --platform manylinux2014_x86_64 --target=package --implementation cp --python-version 3.13.5 --only-binary=:all: --upgrade pymysql

```
Licencia
MIT © 2025 - GMares