from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def home():
    return {"status": "success", "message": "API de test de l'infra"}


@app.get("/ping")
def ping():
    return {"status": "success", "message": "Ping reussi"}