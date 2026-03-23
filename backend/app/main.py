"""
SecureScope AI - Main Application
This module initializes the FastAPI application, configures database tables, and registers API routers.

SecureScope AI is a cybersecurity risk assessment platform that evaluates organizational security posture
through weighted control questionnaires and risk scoring.

Author: Clayton Wherley
Created: 2026-03-10
"""

from fastapi import FastAPI
from app.routes import auth, assessments, simulation 
from app.database import engine, Base
from app.models import user, organization, assessment, question, response, vulnerability, attack_path, attack_step
from app.routers import users, organizations, assessments, auth

"""
    Initializes database tables. 
    
    This command ensures that all SQLAlchemy models registered with the Base metadata are created in the connected
    database if they do not already exist.
"""

Base.metadata.create_all(bind=engine)

app = FastAPI(title="SecureScope AI")

app.include_router(users.router)
app.include_router(organizations.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    """
    Root API endpoint.
    
    Returns a simple message confirming that the SecureScope AI backend is operational.
    
    Returns:
        dict: API status message
    """
    return {"message": "Welcome to SecureScope AI!"}