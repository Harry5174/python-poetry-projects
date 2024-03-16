# type: ignore
import os
from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

# Loaded environment variables from .env file in the root directory
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '.env')
load_dotenv(dotenv_path)

DATABASE_URL = os.getenv("DATABASE_URL")

Base = declarative_base()
engine = create_engine(DATABASE_URL , pool_pre_ping=True)

def create_tables():
    with engine.connect() as connection:
        trans = connection.begin()
        try:
            connection.execute(text("CREATE TABLE IF NOT EXISTS todos (id SERIAL PRIMARY KEY, title VARCHAR(255), description VARCHAR(255))"))
            trans.commit()
            print("Table created successfully.")
        except ProgrammingError as e:
            trans.rollback()
            if "already exists" in str(e):
                print("Table already exists.")
            else:
                print(f"An error occurred: {e}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
