from pydantic_settings import BaseSettings


class BaseHttpSettings(BaseSettings):
    timeout: int = 10
