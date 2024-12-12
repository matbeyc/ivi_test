from dependency_injector import containers, providers

from test_framework.asserts.http import HttpAsserts
from test_framework.core.http.api.chocolate import ChocolateApi
from test_framework.core.http.client import BaseHTTPClient
from test_framework.settings.http.chocolate import ChocolateHttpSettings


class HttpContainer(containers.DeclarativeContainer):
    _chocolate_settings = providers.Singleton(ChocolateHttpSettings)
    _http_client = providers.Factory(BaseHTTPClient, settings=_chocolate_settings)
    chocolate_api = providers.Factory(ChocolateApi, http_client=_http_client)
    http_asserts = providers.Singleton(HttpAsserts)
