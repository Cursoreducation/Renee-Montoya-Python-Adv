import pytest
from .conftest import client
from .conftest import captured_templates
from config import Config


def test_index(client):
    response = client.get('/')

    assert response.status_code == 200
    assert bytes(Config.WEATHER_API_KEY, encoding='utf8') in response.data


def test_text(client):
    response = client.get('/display-text')

    assert response.status_code == 200
    assert b'<title>Text page</title>' in response.data


def test_text_new(client):
    response = client.get('/text/new/')

    assert response.status_code == 200
    assert b'<title>Add Text</title>' in response.data
