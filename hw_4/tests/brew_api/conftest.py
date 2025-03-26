import pytest


# Test API: https://dog.ceo/api
def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://api.openbrewerydb.org/v1/breweries",
        help="This is request url"
    )


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")