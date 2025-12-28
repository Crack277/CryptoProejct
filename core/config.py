from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class CurrencyApi(BaseModel):
    prefix: str = "/v1/cryptocurrency"
    CMC_API_KEY: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_nested_delimiter="__",
    )

    db_username: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str
    db_echo: bool
    api_key: CurrencyApi

    @property
    def db_url(self):
        return (
            f"postgresql+asyncpg://{self.db_username}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )

settings = Settings()