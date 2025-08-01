import cerberus
import requests


def test_api_json_schema(base_url):
    res = requests.get(base_url + "/todos/1")

    schema = {
        "id": {"type": "number"},
        "userId": {"type": "number"},
        "title": {"type": "string"},
        "completed": {"type": "boolean"}
    }

    v = cerberus.Validator()
    assert v.validate(res.json(), schema)
