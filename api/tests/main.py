from fastapi.testclient import TestClient

from api.main import api

client = TestClient(api)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"detail": "Mounted"}
