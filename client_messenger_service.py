# messenger_service.py

import requests
import random
from datetime import datetime
import time
import os
from dotenv import load_dotenv
from logger_config import setup_logger

# Configurar el logger
logger = setup_logger('messenger', 'messenger.log')

# Cargar variables de entorno
load_dotenv()

# Configuración del servicio
SERVICE_NAME = os.getenv("SERVICE2_NAME", "messenger")
TOKEN = os.getenv("SERVICE2_TOKEN")
SERVER_URL = os.getenv("SERVER_URL", "http://localhost:5000/logs")

# Datos de ejemplo para el messenger
USERS = [f"user_{i}" for i in range(1, 1001)]
CHAT_TYPES = ["personal", "grupo", "canal"]
ACTIONS = ["mensaje", "multimedia", "reacción", "videollamada", "archivo"]
FEATURES = ["texto", "imagen", "video", "audio", "documento", "sticker"]

# Mensajes por nivel de severidad
SAMPLE_MESSAGES = {
    "INFO": [
        "Usuario {user1} envió {feature} a {user2}",
        "Nuevo grupo creado por {user1}",
        "Videollamada iniciada en {chat_type}",
        "{user1} compartió archivo en grupo",
        "Nueva reacción de {user1} en mensaje de {user2}",
    ],
    "DEBUG": [
        "Sincronizando mensajes para {user1}",
        "Procesando multimedia de {chat_type}",
        "Verificando estado de conexión de {user1}",
        "Cache actualizado para chat {chat_id}",
    ],
    "WARNING": [
        "Alto uso de almacenamiento en chat {chat_id}",
        "Múltiples reconexiones de {user1}",
        "Latencia elevada en envío de mensajes",
        "Fallos en entrega de mensajes para {user1}",
    ],
    "ERROR": [
        "Error al entregar mensaje a {user1}",
        "Fallo en carga de multimedia en {chat_type}",
        "Error en videollamada {chat_id}",
        "Timeout en sincronización de {user1}",
    ]
}

def generate_log():
    """Genera un log realista del servicio de mensajería"""
    severity = random.choices(
        ["INFO", "DEBUG", "WARNING", "ERROR"],
        weights=[75, 15, 8, 2],  # Mayoría INFO
        k=1
    )[0]
    
    # Generar datos aleatorios
    user1 = random.choice(USERS)
    user2 = random.choice([u for u in USERS if u != user1])
    chat_type = random.choice(CHAT_TYPES)
    feature = random.choice(FEATURES)
    chat_id = random.randint(100000, 999999)
    
    # Seleccionar y formatear mensaje
    message = random.choice(SAMPLE_MESSAGES[severity]).format(
        user1=user1,
        user2=user2,
        chat_type=chat_type,
        feature=feature,
        chat_id=chat_id
    )

    return {
        "timestamp": datetime.now(datetime.UTC).isoformat(),
        "service": SERVICE_NAME,
        "severity": severity,
        "message": message,
    }

def send_logs(logs):
    """Envía los logs al servidor central"""
    headers = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}

    try:
        response = requests.post(SERVER_URL, json=logs, headers=headers)
        if response.status_code == 200:
            logger.info(f"Logs enviados exitosamente: {len(logs)} logs")
        else:
            logger.error(f"Error al enviar logs: {response.status_code} - {response.text}")
    except Exception as e:
        logger.error(f"Error de conexión: {str(e)}")

def main():
    logger.info("Iniciando servicio de Messenger")
    while True:
        # Generar entre 5 y 12 logs (muy activo)
        num_logs = random.randint(5, 12)
        logs = [generate_log() for _ in range(num_logs)]
        
        # Enviar los logs
        send_logs(logs)
        
        # Esperar entre 0.5 y 2 segundos (muy frecuente)
        time.sleep(random.uniform(0.5, 2))

if __name__ == "__main__":
    main()
