from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """System settings for the FastAPI application."""

    PROJECT_NAME: str = "{project}"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"

    # Environment variables
    DEBUG: bool = False
    ENVIRONMENT: str = "development"

    # Pydantic Settings configuration
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )


settings = Settings()
