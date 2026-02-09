from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get():
    response = client.get("/test")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_post():
    response = client.post("/predict?value=5")
    assert response.status_code == 200
    assert "prediction" in response.json()
