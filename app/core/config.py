from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://user:password@postgres/app"
    TEST_DATABASE_URL: str = "postgresql://user:password@postgres/app_test"
    
settings = Settings()
