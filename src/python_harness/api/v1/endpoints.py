from fastapi import APIRouter

from python_harness.services.health import HealthServiceDep

router = APIRouter()


@router.get("/")
async def root() -> dict[str, str]:
    """Root endpoint for the API v1."""
    return {"message": "Welcome to python_harness API v1"}


@router.get("/health")
async def health_check(health_service: HealthServiceDep) -> dict[str, str]:
    """Health check endpoint using HealthService."""
    return health_service.get_status()
