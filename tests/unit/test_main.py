import pytest
from fastapi.testclient import TestClient
from {project}.main import app

client = TestClient(app)

@pytest.mark.unit
def test_read_root():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from {project}!"}

@pytest.mark.unit
def test_read_health():
    """Test the health check endpoint."""
    # This is a unit test for the health endpoint
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
