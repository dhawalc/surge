from pydantic import BaseSettings
from typing import List
import secrets

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    
    # CORS settings
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost", "http://localhost:3000"]

    # Database settings
    DATABASE_URL: str = "postgresql://user:password@postgresserver/db"

    # E-Trade API settings
    ETRADE_CONSUMER_KEY: str = ""
    ETRADE_CONSUMER_SECRET: str = ""
    ETRADE_SANDBOX_MODE: bool = True

    # Robinhood API settings
    ROBINHOOD_USERNAME: str = ""
    ROBINHOOD_PASSWORD: str = ""

    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()