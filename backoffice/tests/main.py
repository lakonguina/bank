from fastapi.testclient import TestClient

from backoffice.main import api

client = TestClient(api)

