from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Cabin Management System"
    app_env: str = "development"


settings = Settings()
