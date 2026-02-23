from fastapi import FastAPI
from app.routes import auth, assessments, simulation # Example routes
from app.database import engine, Base
from app.models import user, organization, assessment, question, response, vulnerability, attack_path, attack_step # Import all your models
from app.routers import users, organizations, assessments # Import Routers

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="SecureScope AI")

app.include_router(users.router)
app.include_router(organizations.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to SecureScope AI!"}