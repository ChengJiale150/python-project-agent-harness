import pytest
from fastapi.testclient import TestClient
from {project}.main import app

client = TestClient(app)

@pytest.mark.e2e
def test_full_api_workflow():
    """End-to-end test for the API workflow."""
    # Check root
    root_response = client.get("/")
    assert root_response.status_code == 200

    # Check health
    health_response = client.get("/health")
    assert health_response.status_code == 200
    assert health_response.json()["status"] == "ok"
