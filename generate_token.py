import jwt
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Obtener la clave secreta del .env
SECRET_KEY = os.getenv("JWT_SECRET_KEY")
SERVICE_NAME = os.getenv("SERVICE1_NAME", "servicio1")

payload = {
    "service": SERVICE_NAME,
    "exp": datetime.utcnow() + timedelta(hours=2),  # expira en 2 horas
}

token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
print(token)
