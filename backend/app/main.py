from fastapi import FastAPI
from app.routes import auth, assessments, simulation # Example routes

app = FastAPI(title="SecureScope AI")

@app.get("/")
def read_root():
    return {"message": "Welcome to SecureScope AI!"}