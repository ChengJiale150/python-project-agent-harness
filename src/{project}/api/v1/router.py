from fastapi import APIRouter
from {project}.api.v1 import endpoints

api_router = APIRouter()
api_router.include_router(endpoints.router, prefix="/base", tags=["base"])
