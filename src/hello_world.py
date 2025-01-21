# Import FastAPI
from fastapi import FastAPI

# Create an instance of FastAPI
app = FastAPI()


# Define API route
@app.get("/")  # Decorator to define the route
async def root():  # Function to be executed when the route is called
    return {"message": "Hello World!"}  # JSON response
