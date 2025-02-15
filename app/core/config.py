from pydantic import BaseSettings


class Settings(BaseSettings):
    database_uri: str
    secret_key: str
    environment: str = "development"

    class Config:
        env_file = ".env"

settings = Settings()