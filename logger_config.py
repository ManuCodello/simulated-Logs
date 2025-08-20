import logging
import os
from datetime import datetime


def setup_logger(name, log_file, level=logging.INFO):
    """Configuración de un logger con archivo y consola"""

    # Crear el directorio logs si no existe
    os.makedirs("logs", exist_ok=True)

    # Crear formateador
    formatter = logging.Formatter(
        "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
    )

    # Configurar el handler para archivo
    file_handler = logging.FileHandler(f"logs/{log_file}")
    file_handler.setFormatter(formatter)

    # Configurar el handler para consola
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Configurar el logger
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
