import requests
import pytest

# WARNING Bad Example: (Never use sensitive data like this!)
AUTH_DATA = {"login": "admin", "password": "admin"}


def test_init_database(base_url):
    session = requests.Session()
    session.request("login", "https://run.mocky.io/v3/833da713-e93c-423d-b1d4-20679b67ca53", json=AUTH_DATA)
    response = session.request("create", "{}/create/init".format(base_url))
    assert response.json().get("status") == "created"


def test_reinit_database(base_url):
    session = requests.Session()
    session.request("login", "https://run.mocky.io/v3/833da713-e93c-423d-b1d4-20679b67ca53", json=AUTH_DATA)
    response = requests.request("recreate", "{}/create/reinit".format(base_url))
    assert response.json().get("status") == "table dropped and created"