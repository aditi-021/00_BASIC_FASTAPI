#to load env variable in python project
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    DATABASE_URL: str
    OPENAI_API_KEY: str
    ANTHROPIC_API_KEY: str
    DEBUG : bool = True
    AUTH_SECRET_KEY: str

setting = Settings()