from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

try:
    engine = create_engine(DATABASE_URL)
    conn = engine.connect()
    print("Connection Successful!")
except Exception as e:
    print(f"Connection Failed:", e)