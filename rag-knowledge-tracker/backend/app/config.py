
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    snowflake_account: str
    snowflake_user: str
    snowflake_password: str
    
    class Config:
        env_file = ".env"

settings = Settings()
