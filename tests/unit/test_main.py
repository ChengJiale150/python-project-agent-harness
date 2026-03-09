import pytest
from fastapi import status
from fastapi.testclient import TestClient
from {project}.main import app
from {project}.core.config import settings

client = TestClient(app)


@pytest.mark.unit
def test_read_root():
    """Test the root endpoint of API v1."""
    response = client.get(f"{settings.API_V1_STR}/base/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": f"Welcome to {settings.PROJECT_NAME} API v1"}


@pytest.mark.unit
def test_read_health():
    """Test the health check endpoint of API v1."""
    response = client.get(f"{settings.API_V1_STR}/base/health")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "ok", "version": settings.VERSION}
