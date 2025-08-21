import jwt
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from pathlib import Path


def generate_token(service_name, secret_key, hours=24):
    """Genera un token JWT para un servicio específico"""
    payload = {
        "service": service_name,
        "exp": datetime.now(datetime.UTC) + timedelta(hours=hours),
    }
    return jwt.encode(payload, secret_key, algorithm="HS256")


def update_env_token(service_num, token):
    """Actualiza el token en el archivo .env de forma segura"""
    env_path = Path(".env")
    temp_path = Path(".env.tmp")

    with env_path.open("r") as env_file, temp_path.open("w") as temp_file:
        for line in env_file:
            if f"SERVICE{service_num}_TOKEN=" in line:
                temp_file.write(f'SERVICE{service_num}_TOKEN="{token}"\n')
            else:
                temp_file.write(line)

    temp_path.replace(env_path)


def main():
    # Cargar variables de entorno
    load_dotenv()

    # Obtener la clave secreta
    secret_key = os.getenv("JWT_SECRET_KEY")
    if not secret_key:
        print("Error: JWT_SECRET_KEY no encontrada en .env")
        return

    # Generar tokens para ambos servicios
    services = [
        (1, "marketplace", os.getenv("SERVICE1_NAME", "marketplace")),
        (2, "messenger", os.getenv("SERVICE2_NAME", "messenger")),
    ]

    for service_num, service_type, service_name in services:
        # Generar nuevo token
        token = generate_token(service_name, secret_key)

        # Actualizar el archivo .env
        update_env_token(service_num, token)

        print(f"\nToken generado para {service_type.upper()}:")
        print(f"SERVICE{service_num}_TOKEN={token}")


if __name__ == "__main__":
    main()
