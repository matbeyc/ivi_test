from pydantic_settings import SettingsConfigDict

from test_framework.settings.http.base import BaseHttpSettings


class ChocolateHttpSettings(BaseHttpSettings):
    host: str = "http://chocolate:8080"
    model_config = SettingsConfigDict(env_prefix="APP_CHOCOLATE_")
