import requests
import pytest


def test_get_all_breweries(base_url):
    response = requests.get(base_url)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


@pytest.mark.parametrize("country, total", [('South Korea', '61'), ('Scotland', '10')])
def test_get_metadata_by_country(base_url, country, total):
    response = requests.get(base_url + '/meta',
                            params={'by_country': country})
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert isinstance(data, dict)
    assert data['total'] == total


@pytest.mark.parametrize("amount", [4, 6, 10])
def test_get_random_amount_breweries(base_url, amount):
    response = requests.get(base_url + '/random',
                            params={'size': amount})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == amount


@pytest.mark.parametrize("country", ["United States", "England", "Ireland"])
def test_get_breweries_by_country(base_url, country):
    response = requests.get(base_url,
                            params={'by_country': country})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    for brewery in data:
        assert 'country' in brewery
        assert brewery['country'] == country


@pytest.mark.parametrize("city,brewery_type", [("Brighton", "brewpub"), ("Austin", "micro")])
def test_get_breweries_by_city_and_type(base_url, city, brewery_type):
    response = requests.get(base_url,
                            params={'by_city': city, 'by_type': brewery_type})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    for brewery in data:
        assert city in brewery['city']
        assert brewery_type in brewery['brewery_type']
