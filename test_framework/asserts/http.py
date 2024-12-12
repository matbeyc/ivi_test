from typing import Type

from pydantic import BaseModel
from requests import Response

from test_framework.asserts.base import BaseAsserts
from test_framework.schemas.enums import StatusCode


class HttpAsserts(BaseAsserts):
    @staticmethod
    def assert_response_schema(
        response: Response, expected_status_code: StatusCode, schema: Type[BaseModel]
    ):
        assert response.status_code == expected_status_code
        schema.model_validate(response.json())
