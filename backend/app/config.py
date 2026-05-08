from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Cabin Management System"
    app_env: str = "development"

    database_host: str = "localhost"
    database_port: int = 5432
    database_name: str = "cabins_db"
    database_user: str = "cabins_app"
    database_password: str = "cabins_password"

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg://{self.database_user}:"
            f"{self.database_password}@{self.database_host}:"
            f"{self.database_port}/{self.database_name}"
        )


settings = Settings()
