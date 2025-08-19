# Sistema de Logging Distribuido

Este es un sistema simple de logging distribuido que consiste en:
1. Un servidor central que recibe y almacena logs
2. Servicios simulados que generan y envían logs

## Estructura del Proyecto

```
flaskproject/
├── server.py           # Servidor central de logging
├── service_simulator.py # Simulador de servicios que generan logs
├── logs.db            # Base de datos SQLite (se crea automáticamente)
└── README.md          # Este archivo
```

## Requisitos

- Python 3.x
- Flask
- requests
- python-dotenv

## Configuración

1. Instala las dependencias:
```bash
pip install flask requests python-dotenv
```

2. Los tokens válidos están definidos en `server.py`:
```python
VALID_TOKENS = ['token_servicio1', 'token_servicio2', 'token_servicio3']
```

## Uso

1. Inicia el servidor central:
```bash
python server.py
```
El servidor se iniciará en `http://localhost:5000`

2. Inicia uno o más servicios simulados:
```bash
python service_simulator.py
```

Cada servicio simulado generará logs aleatorios y los enviará al servidor.

## API Endpoints

### POST /logs
Recibe logs de los servicios.

Headers requeridos:
- `Authorization: Token <token>`
- `Content-Type: application/json`

Formato del body:
```json
{
    "timestamp": "2023-08-18T12:00:00",
    "service": "servicio1",
    "severity": "INFO",
    "message": "Mensaje del log"
}
```

### GET /logs
Consulta logs con filtros opcionales.

Headers requeridos:
- `Authorization: Token <token>`

Parámetros de query opcionales:
- `timestamp_start`: Fecha inicial (ISO format)
- `timestamp_end`: Fecha final (ISO format)
- `received_at_start`: Fecha de recepción inicial
- `received_at_end`: Fecha de recepción final

## Ejemplos de Uso

### Enviar un log:
```bash
curl -X POST http://localhost:5000/logs \
  -H "Authorization: Token token_servicio1" \
  -H "Content-Type: application/json" \
  -d '{
    "timestamp": "2023-08-18T12:00:00",
    "service": "servicio1",
    "severity": "INFO",
    "message": "Test log"
  }'
```

### Consultar logs:
```bash
curl http://localhost:5000/logs \
  -H "Authorization: Token token_servicio1" \
  -G \
  --data-urlencode "timestamp_start=2023-08-18T00:00:00" \
  --data-urlencode "timestamp_end=2023-08-18T23:59:59"
```
