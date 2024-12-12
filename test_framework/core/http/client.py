import requests
from requests import Response
from requests.adapters import HTTPAdapter

from test_framework.settings.http.base import BaseHttpSettings


class BaseHTTPClient:
    def __init__(self, settings: BaseHttpSettings):
        self._settings = settings
        self._session = requests.Session()
        self._session.mount("http://", HTTPAdapter(max_retries=0))
        self._session.mount("https://", HTTPAdapter(max_retries=0))

    def get(self, endpoint, **request_params):
        return self._send_request(
            endpoint=endpoint, method="GET", request_params=request_params
        )

    def post(self, endpoint, **request_params):
        return self._send_request(
            endpoint=endpoint, method="POST", request_params=request_params
        )

    def _configure_request(self, endpoint: str, method: str, request_params) -> dict:
        url = f"{self._settings.host}/{endpoint}"
        result_request_params = dict(
            method=method,
            url=url,
            verify=False,
            data=request_params.get("data"),
            json=request_params.get("json"),
            auth=request_params.get("auth"),
            headers=request_params.get("headers"),
            timeout=self._settings.timeout,
        )
        return result_request_params

    def _send_request(self, endpoint, method, **request_params) -> Response:
        request_params = self._configure_request(endpoint, method, **request_params)
        return self._session.request(**request_params)
