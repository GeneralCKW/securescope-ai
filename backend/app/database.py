"""
    Database configuration module.
    
    This module initializes the SQLAlchemy engine, session factory, and base class used 
    for defining database models.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("Database_URL is not set in your .env file")

""" 
SQLAlchemy engine used to connect to the PostgreSQL database.
"""
engine = create_engine(DATABASE_URL)

"""
Session factory used to create database sessions.
"""
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

"""
Base class for all database models.
"""
Base = declarative_base()

def get_db():
    """
    Provides a database session to API routes.
    
    This is used as a FastAPI dependency to ensure each request receives its own database
    session which is properly closed after use.
    
    Yields:
        Session: SQLAlchemy database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()