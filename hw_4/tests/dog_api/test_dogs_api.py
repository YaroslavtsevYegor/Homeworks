import requests
import pytest


def test_all_breeds_list(base_url):
    response = requests.get(base_url + "/breeds/list/all")
    data = response.json()
    assert response.status_code == 200
    assert data['status'] == 'success'
    assert 'message' in data
    assert isinstance(data['message'], dict)


def test_random_dog_image(base_url):
    response = requests.get(base_url + "/breeds/image/random")
    data = response.json()
    assert response.status_code == 200
    assert data['status'] == 'success'
    assert 'message' in data
    assert data['message'].endswith('.jpg')


@pytest.mark.parametrize("breed", ["borzoi", "chihuahua", "ovcharka"])
def test_breed_images(base_url, breed):
    response = requests.get(base_url + f"/breed/{breed}/images")
    data = response.json()
    assert response.status_code == 200
    assert data['status'] == 'success'
    assert 'message' in data
    assert isinstance(data['message'], list)
    assert len(data['message']) > 0
    for image in data['message']:
        assert breed in image


@pytest.mark.parametrize("breed, amount", [("pitbull", 5), ("husky", 6), ("samoyed", 7)])
def test_random_breed_image_with_amount(base_url, breed, amount):
    response = requests.get(base_url + f"/breed/{breed}/images/random/{amount}")
    data = response.json()
    assert response.status_code == 200
    assert data['status'] == 'success'
    assert 'message' in data
    assert isinstance(data['message'], list)
    assert len(data['message']) == amount
    for image in data['message']:
        assert breed in image


@pytest.mark.parametrize("sub_breed, breed", [("english", 'mastiff'), ("cocker", 'spaniel'), ("yorkshire", 'terrier')])
def test_sub_breed_in_breed(base_url, breed, sub_breed):
    response = requests.get(base_url + f"/breed/{breed}/list")
    data = response.json()
    assert response.status_code == 200
    assert data['status'] == 'success'
    assert 'message' in data
    assert isinstance(data['message'], list)
    assert sub_breed in data['message']
