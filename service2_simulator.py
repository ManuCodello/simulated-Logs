import requests
import random
from datetime import datetime
import time

# Load environment variables
from dotenv import load_dotenv
import os

load_dotenv()

SERVICE_NAME = os.getenv("SERVICE2_NAME")
TOKEN = os.getenv("SERVICE2_TOKEN")
SERVER_URL = os.getenv("SERVER_URL", "http://localhost:5000/logs")

SAMPLE_MESSAGES = {
    "INFO": ["Usuario ha muerto", "Transacción completada"],
    "DEBUG": ["Verificando conexión", "Procesando solicitud"],
    "ERROR": ["Error de validación, murio usuario", "Timeout en servicio externo"],
    "WARNING": ["Uso de memoria alto", "Espacio en disco bajo"],
}


def generate_log():
    severity = random.choices(
        ["INFO", "DEBUG", "WARNING", "ERROR"], weights=[60, 25, 10, 5], k=1
    )[0]
    message = random.choice(SAMPLE_MESSAGES[severity])
    return {
        "timestamp": datetime.now().isoformat(),
        "service": SERVICE_NAME,
        "severity": severity,
        "message": message,
    }


def send_logs(logs):
    headers = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
    try:
        response = requests.post(SERVER_URL, json=logs, headers=headers)
        print(response.json())
    except Exception as e:
        print(f"Error de conexión: {str(e)}")


def main():
    while True:
        logs = [generate_log() for _ in range(random.randint(1, 5))]
        send_logs(logs)
        time.sleep(random.uniform(2, 5))


if __name__ == "__main__":
    main()
