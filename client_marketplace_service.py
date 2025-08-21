# marketplace_service.py

import requests
import random
from datetime import datetime
import time
import os
from dotenv import load_dotenv
from logger_config import setup_logger

# Configurar el logger
logger = setup_logger('marketplace', 'marketplace.log')

# Cargar variables de entorno
load_dotenv()

# Configuración del servicio
SERVICE_NAME = os.getenv("SERVICE1_NAME", "marketplace")
TOKEN = os.getenv("SERVICE1_TOKEN")
SERVER_URL = os.getenv("SERVER_URL", "http://localhost:5000/logs")

# Datos de ejemplo para el marketplace
PRODUCTS = ["Smartphone", "Laptop", "Headphones", "Smart TV", "Tablet", "Smartwatch"]
ACTIONS = ["view", "add_to_cart", "purchase", "review", "wishlist"]
USERS = [f"user_{i}" for i in range(1, 1001)]  # Simular 1000 usuarios

# Mensajes por nivel de severidad
SAMPLE_MESSAGES = {
    "INFO": [
        "Usuario {user} visualizó {product}",
        "Usuario {user} agregó {product} al carrito",
        "Compra exitosa: {product} por {user}",
        "Nueva reseña de {product} por {user}",
        "Producto {product} añadido a lista de deseos",
    ],
    "DEBUG": [
        "Cargando catálogo de productos",
        "Actualizando inventario de {product}",
        "Procesando pago para orden #{order_id}",
        "Verificando stock de {product}",
    ],
    "WARNING": [
        "Stock bajo para {product}: solo 5 unidades",
        "Alto tráfico en la categoría de {product}",
        "Múltiples intentos fallidos de pago por {user}",
        "Tiempo de respuesta elevado en búsquedas",
    ],
    "ERROR": [
        "Error en proceso de pago para {user}",
        "Fallo al actualizar inventario de {product}",
        "Error en sincronización de precios",
        "Timeout en procesamiento de orden #{order_id}",
    ]
}

def generate_log():
    severity = random.choices(
        ["INFO", "DEBUG", "WARNING", "ERROR"],
        weights=[70, 20, 8, 2],  # La mayoría serán INFO
        k=1
    )[0]
    
    # Generar datos aleatorios
    user = random.choice(USERS)
    product = random.choice(PRODUCTS)
    order_id = random.randint(10000, 99999)
    
    # Seleccionar y formatear mensaje
    message = random.choice(SAMPLE_MESSAGES[severity]).format(
        user=user,
        product=product,
        order_id=order_id
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
    logger.info("Iniciando servicio de Marketplace")
    while True:
        # Generar entre 3 y 8 logs (más actividad que antes)
        num_logs = random.randint(3, 8)
        logs = [generate_log() for _ in range(num_logs)]
        
        # Enviar los logs
        send_logs(logs)
        
        # Esperar entre 1 y 3 segundos (más frecuente que antes)
        time.sleep(random.uniform(1, 3))

if __name__ == "__main__":
    main()
