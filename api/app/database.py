from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import PostgresDsn
import os
from dotenv import load_dotenv

if os.environ.get("PYTHON_ENV") == "development":
    load_dotenv()

DATABASE_URL = PostgresDsn.build(
    scheme="postgresql",
    user=os.environ.get("DB_USERNAME"),
    password=os.environ.get("DB_PASSWORD"),
    host=os.environ.get("DB_HOST"),
    port=os.environ.get("DB_PORT"),
    path=f"/{os.environ.get('DB_DATABASE')}",
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
