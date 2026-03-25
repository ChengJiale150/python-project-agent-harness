from fastapi import APIRouter

from python_harness.api.v1 import endpoints

api_router = APIRouter()
api_router.include_router(endpoints.router, prefix="/base", tags=["base"])
