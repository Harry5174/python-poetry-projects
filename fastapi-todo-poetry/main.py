# main.py

# Import statements for modules within the project
from src.todo.database.database_operations import engine, Base, create_tables
from src.todo.routes.main import app

# Create database tables
# def create_tables():
#     Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    # Create database tables before running the app
    create_tables()
    
    # Run the FastAPI app
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
