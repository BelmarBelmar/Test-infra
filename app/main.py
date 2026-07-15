import os
from fastapi import FastAPI
import psycopg2


app = FastAPI()

DB_HOST = os.getenv("DB_HOST", "")
DB_PORT = os.getenv("DB_PORT", "")
DB_NAME = os.getenv("DB_NAME", "")
DB_USER = os.getenv("DB_USER", "")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")


@app.get("/")
def home():
    return {"status": "success", "message": "API de test de l'infra"}


@app.get("/ping")
def ping():
    return {"status": "success", "message": "Ping reussi"}


@app.get("/db-test")
def test_db_connection():
    try:
        # Tentative de connexion au serveur Postgres mutualisé
        connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            connect_timeout=3
        )
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        cursor.close()
        connection.close()
        
        return {
            "status": "success",
            "message": "Connexion à PostgreSQL réussie !",
            "postgres_version": db_version[0]
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Échec de la connexion : {str(e)}"
        }
