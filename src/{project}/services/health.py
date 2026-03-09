from typing import Annotated
from fastapi import Depends
from {project}.core.config import settings
from {project}.services.base import BaseServiceDep


class HealthService:
    """Service to handle health checks."""

    def __init__(self, base_service: BaseServiceDep) -> None:
        """Initialize health service with base service."""
        self.base_service = base_service

    def get_status(self) -> dict[str, str]:
        """Get the current API status and version."""
        return {"status": "ok", "version": settings.VERSION}


def get_health_service(base_service: BaseServiceDep) -> HealthService:
    """Dependency provider for HealthService."""
    return HealthService(base_service)


HealthServiceDep = Annotated[HealthService, Depends(get_health_service)]
