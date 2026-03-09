import pytest
from fastapi import status
from fastapi.testclient import TestClient
from {project}.main import app

client = TestClient(app)

@pytest.mark.e2e
def test_full_api_workflow():
    """End-to-end test for the API workflow."""
    # Check root
    root_response = client.get("/")
    assert root_response.status_code == status.HTTP_200_OK

    # Check health
    health_response = client.get("/health")
    assert health_response.status_code == status.HTTP_200_OK
    assert health_response.json()["status"] == "ok"
