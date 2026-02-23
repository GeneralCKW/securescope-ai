from fastapi import FastAPI
from app.routes import auth, assessments, simulation # Example routes
from app.database import engine, Base
from app.models import user # Import all your models

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="SecureScope AI")

@app.get("/")
def read_root():
    return {"message": "Welcome to SecureScope AI!"}