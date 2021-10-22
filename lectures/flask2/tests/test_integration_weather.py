import pytest
from .conftest import client

def test_weather(client):
    response = client.get('/weather?city=Kiev')
    assert response.status_code == 200
    assert response.json['location']['name'] == "Kiev"