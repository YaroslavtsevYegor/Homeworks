import pytest


@pytest.fixture(params=[4, 5, 6], ids=["four", "five", "six"])
def param_fixture(request):
    return request.param


@pytest.fixture
def fixt(request):
    return request.param * 3


@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com"
