from pydantic import BaseModel
from pydantic_settings import BaseSettings


class RunSettings(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000


class ApiPrefix(BaseModel):
    prefix: str = "/api"


class Settings(BaseSettings):
    run: RunSettings = RunSettings()
    api: ApiPrefix = ApiPrefix()


settings = Settings()