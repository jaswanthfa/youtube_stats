from fastapi import FastAPI
from routes import router  # Import the router from routes.py

# Initialize FastAPI app
app = FastAPI()

# Include the router from routes.py
app.include_router(router)

# Run the server with: uvicorn main:app --reload