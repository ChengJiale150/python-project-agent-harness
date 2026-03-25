import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from python_harness.api.v1.router import api_router
from python_harness.core.config import settings


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    application = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
    )

    # Set all CORS enabled origins
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include API routers
    application.include_router(api_router, prefix=settings.API_V1_STR)

    return application


app = create_app()


def main() -> None:
    """Entry point for the project."""
    uvicorn.run(
        "python_harness.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
    )


if __name__ == "__main__":
    main()
