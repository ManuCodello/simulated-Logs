#server.py 

from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime
import jwt
import os
from dotenv import load_dotenv
from logger_config import setup_logger

# Configurar el logger
logger = setup_logger('server', 'server.log')

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Get secret key from environment variable
SECRET_KEY = os.getenv('JWT_SECRET_KEY')

# Lista de tokens válidos (en producción esto debería estar en una base de datos o variable de entorno)
# VALID_TOKENS = ["token_servicio1", "token_servicio2", "token_servicio3"]

def valid_jwt(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        logger.info(f"Token válido para el servicio: {payload.get('service')}")
        return payload  # devuelve los datos del token si es válido
    except jwt.ExpiredSignatureError:
        logger.error("Token expirado")
        return None  # token expirado
    except jwt.InvalidTokenError:
        logger.error("Token inválido")
        return None  # token inválido

def init_db():
    with sqlite3.connect("logs.db") as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                service TEXT NOT NULL,
                severity TEXT NOT NULL,
                message TEXT NOT NULL,
                received_at TEXT NOT NULL
            )
        """)


def validate_token(token):
    # Extraer el token del header 'Authorization: Bearer token'
    if not token or not token.startswith("Bearer "):
        return False, " Token no es valido"
    token = token.split(" ")[1]
    return token


@app.route("/logs", methods=["POST"])
def receive_logs():
    # Verificar el token de autorización
    auth_header = request.headers.get("Authorization")
    if not validate_token(auth_header):
        return jsonify({"error": "¿Quién sos bro, tu no eres peter parker"}), 401
    
    token = auth_header.split(" ")[1]
    payload = valid_jwt(token)
    if not payload:
        return jsonify({"error": "Token inválido o expirado"}), 401

    # Obtener los logs del request
    logs = request.json
    if not isinstance(logs, list):
        logs = [logs]  # Si es un solo log, convertirlo a lista

    try:
        with sqlite3.connect("logs.db") as conn:
            cursor = conn.cursor()
            # Insertar cada log en la base de datos
            for log in logs:
                cursor.execute(
                    """INSERT INTO logs (timestamp, service, severity, message, received_at)
                    VALUES (?, ?, ?, ?, ?)""",
                    (
                        log["timestamp"],
                        log["service"],
                        log["severity"],
                        log["message"],
                        datetime.now(datetime.UTC).isoformat(),
                    ),
                )
        return jsonify({"message": f"Se guardaron {len(logs)} logs correctamente"}), 200
    except Exception as e:
        return jsonify({"error": f"Error al guardar los logs: {str(e)}"}), 500


@app.route("/logs", methods=["GET"])
def get_logs():
    # Verificar el token de autorización
    auth_header = request.headers.get("Authorization")
    if not validate_token(auth_header):
        return jsonify({"error": "¿Quién sos, bro?"}), 401

    # Obtener parámetros de filtro
    timestamp_start = request.args.get("timestamp_start")
    timestamp_end = request.args.get("timestamp_end")
    received_at_start = request.args.get("received_at_start")
    received_at_end = request.args.get("received_at_end")

    query = "SELECT * FROM logs WHERE 1=1"
    params = []

    if timestamp_start:
        query += " AND timestamp >= ?"
        params.append(timestamp_start)
    if timestamp_end:
        query += " AND timestamp <= ?"
        params.append(timestamp_end)
    if received_at_start:
        query += " AND received_at >= ?"
        params.append(received_at_start)
    if received_at_end:
        query += " AND received_at <= ?"
        params.append(received_at_end)

    query += " ORDER BY timestamp DESC"

    try:
        with sqlite3.connect("logs.db") as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(query, params)
            logs = [dict(row) for row in cursor.fetchall()]
            return jsonify(logs), 200
    except Exception as e:
        return jsonify({"error": f"Error al consultar los logs: {str(e)}"}), 500

if __name__ == "__main__":
    init_db()  # Inicializar la base de datos
    app.run(debug=True, port=5000)


