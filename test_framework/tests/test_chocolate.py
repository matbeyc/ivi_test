import random

from test_framework.schemas.enums import StatusCode, ResponseMessage, AssertMode
from test_framework.schemas.models.response import Chocolates, ChocolatePrice, Error


class TestChocolate:

    def test_get_chocolates(self, http_container):
        response = http_container.chocolate_api().get_chocolates()
        http_container.http_asserts().assert_response_schema(
            response, StatusCode.OK, Chocolates
        )

    def test_get_price_of_existing_chocolate(self, http_container, chocolate):
        response = http_container.chocolate_api().get_chocolate_price(chocolate.id)
        http_container.http_asserts().assert_response_schema(
            response, StatusCode.OK, ChocolatePrice
        )

    def test_get_price_of_not_existing_chocolate(self, http_container):
        response = http_container.chocolate_api().get_chocolate_price(
            random.randint(1000, 100000)
        )
        http_container.http_asserts().assert_response_schema(
            response, StatusCode.NOT_FOUND, Error
        )
        http_container.http_asserts().assert_models(
            Error(error=ResponseMessage.CHOCOLATE_NOT_FOUND),
            Error(**response.json()),
            AssertMode.FULL,
        )

    def test_buy_not_existing_chocolate(self, http_container):
        response = http_container.chocolate_api().buy_chocolate(
            random.randint(1000, 100000)
        )
        http_container.http_asserts().assert_response_schema(
            response, StatusCode.NOT_FOUND, Error
        )
        http_container.http_asserts().assert_models(
            Error(error=ResponseMessage.CHOCOLATE_NOT_FOUND),
            Error(**response.json()),
            AssertMode.FULL,
        )

    def test_buy_chocolate(self, http_container):
        pass

    def test_buy_chocolate_with_insufficient_balance(self, http_container):
        pass
