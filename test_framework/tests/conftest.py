import pytest

from test_framework.containers.containers import HttpContainer
from test_framework.schemas.models.response import Chocolate


@pytest.fixture(scope="session")
def http_container() -> HttpContainer:
    return HttpContainer()


@pytest.fixture(scope="function")
def chocolate() -> Chocolate:
    yield Chocolate(id=1, name="Аленка", price=55.0)
