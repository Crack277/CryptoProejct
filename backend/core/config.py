from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class CurrencyApi(BaseModel):
    prefix: str = "/v1"
    CMC_API_KEY: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env_example",
        case_sensitive=False,
        env_nested_delimiter="__",
    )
    api_key: CurrencyApi

settings = Settings()