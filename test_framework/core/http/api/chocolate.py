from requests import Response

from test_framework.core.http.client import BaseHTTPClient
from test_framework.schemas.enums import ChocolateEndpoint


class ChocolateApi:
    def __init__(self, http_client: BaseHTTPClient):
        self._client = http_client

    def get_chocolates(self) -> Response:
        return self._client.get(ChocolateEndpoint.GET_CHOCOLATES)

    def get_chocolate_price(self, chocolate_id: int):
        return self._client.get(
            ChocolateEndpoint.GET_CHOCOLATE_PRICE.format(chocolate_id=chocolate_id)
        )

    def buy_chocolate(self, chocolate_id: str):
        return self._client.post(
            ChocolateEndpoint.BUY_CHOCOLATE.format(chocolate_id=chocolate_id)
        )
