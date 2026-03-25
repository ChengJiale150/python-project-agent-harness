from typing import Annotated

from fastapi import Depends


class BaseService:
    """Base service class for shared logic."""

    def __init__(self) -> None:
        """Initialize base service."""


def get_base_service() -> BaseService:
    """Dependency provider for BaseService."""
    return BaseService()


BaseServiceDep = Annotated[BaseService, Depends(get_base_service)]
