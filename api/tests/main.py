from fastapi.testclient import TestClient

from api.main import api

client = TestClient(api)

