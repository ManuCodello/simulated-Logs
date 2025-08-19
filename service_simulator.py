# service_simulator.py 

import requests
import random
from datetime import datetime
import time

# Configuración del servicio
SERVICE_NAME = "servicio1"  # Cambia esto para cada servicio
TOKEN = "token_servicio1"  # Usa el token correspondiente al servicio
SERVER_URL = "http://localhost:5000/logs"

# Lista de mensajes de ejemplo para cada nivel de severidad
SAMPLE_MESSAGES = {
    "INFO": [
        "Usuario ha iniciado sesión",
        "Transacción completada exitosamente",
        "Proceso de respaldo iniciado",
        "Sincronización de datos completada",
    ],
    "DEBUG": [
        "Verificando conexión a la base de datos",
        "Procesando solicitud del usuario",
        "Cargando configuración del sistema",
        "Iniciando proceso en segundo plano",
    ],
    "WARNING": [
        "Uso de memoria alto",
        "Espacio en disco bajo",
        "Intentos fallidos de autenticación",
        "Conexión inestable detectada",
    ],
    "ERROR": [
        "Error al conectar con la base de datos",
        "Timeout en la solicitud al servicio externo",
        "Error de validación en formulario",
        "Proceso interrumpido inesperadamente",
    ],
    
}


def generate_log():
    """Genera un log aleatorio con datos realistas"""
    severity = random.choices(["INFO", "DEBUG", "WARNING", "ERROR"], weights=[80,50,15,5], k=1)[0]
    message = random.choice(SAMPLE_MESSAGES[severity])

    return {
        "timestamp": datetime.now().isoformat()[:-2],
        "service": SERVICE_NAME,
        "severity": severity,
        "message": message,
    }


def send_logs(logs):
    """Envía los logs al servidor central"""
    headers = {"Authorization": f"Token {TOKEN}", "Content-Type": "application/json"}

    try:
        response = requests.post(SERVER_URL, json=logs, headers=headers)
        if response.status_code == 200:
            print(f"Logs enviados exitosamente: {len(logs)} logs")
        else:
            print(f"Error al enviar logs: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error de conexión: {str(e)}")

def main():
    print(f"Iniciando servicio de logs: {SERVICE_NAME}")
    while True:
        # Generar entre 1 y 5 logs
        num_logs = random.randint(1, 5)
        logs = [generate_log() for _ in range(num_logs)]

        # Enviar los logs
        send_logs(logs)

        # Esperar entre 2 y 5 segundos antes de la siguiente generación
        wait_time = random.uniform(2, 5)
        time.sleep(wait_time)




if __name__ == "__main__":
    main()
