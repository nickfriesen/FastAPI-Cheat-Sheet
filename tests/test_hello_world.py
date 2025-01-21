from fastapi.testclient import TestClient
from src.hello_world import app

# Create a test client using the FastAPI instance
client = TestClient(app)


# Define test function
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}
