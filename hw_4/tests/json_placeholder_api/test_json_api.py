import requests
import pytest


@pytest.mark.parametrize("post_id", [1, 12, 23])
def test_get_comments_by_post_id(base_url, post_id):
    response = requests.get(base_url + "/comments",
                            params={'postId': post_id})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    for comment in data:
        assert 'postId' in comment
        assert comment['postId'] == post_id


@pytest.mark.parametrize("id, title, body, userId",
                         [(2, 'update title', 'update body', 3),
                          (6, 'title update', '', 5)])
def test_put_request(base_url, id, title, body, userId):
    put_request_json = {
        "id": id,
        "title": title,
        "body": body,
        "userId": userId
    }
    response = requests.put(base_url + f"/posts/{id}",
                            json=put_request_json)
    data = response.json()
    assert response.status_code == 200
    assert data["id"] == put_request_json["id"]
    assert data["title"] == put_request_json["title"]
    assert data["body"] == put_request_json["body"]
    assert data["userId"] == put_request_json["userId"]


@pytest.mark.parametrize("id, parameter,value",
                         [(2, 'title', 'update title'),
                          (6, 'body', 'update body'),
                          (9, 'userId', '20')])
def test_patch_request(base_url, id, parameter, value):
    patch_request_json = {
        parameter: value
    }
    response = requests.patch(base_url + f"/posts/{id}",
                              json=patch_request_json)
    data = response.json()
    assert response.status_code == 200
    assert data["id"] == id
    assert data[parameter] == patch_request_json[parameter]


@pytest.mark.parametrize("post_id", [1, 44])
def test_delete_request(base_url, post_id):
    url = base_url + f'/posts/{post_id}'
    response = requests.delete(url)
    assert response.status_code == 200
    assert response.request.method == "DELETE"


@pytest.mark.parametrize("id", [4, 5, 6])
def test_get_any_user_todo_is_done(base_url, id):
    response = requests.get(base_url + f"/users/{id}/todos")
    assert response.status_code == 200
    data = response.json()
    for value in data:
        assert value["userId"] == id
    assert any(todo['completed'] for todo in data)
