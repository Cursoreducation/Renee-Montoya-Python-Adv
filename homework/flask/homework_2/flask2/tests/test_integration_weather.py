import pytest
from .conftest import client


def test_integration_weather(client):
    response = client.get('/weather?city=Kiev')

    assert response.status_code == 200
    assert response.json['location']['name'] == "Kiev"


def test_integration_get_your_weather(client):
    response = client.get('/get-your-weather')

    assert response.status_code == 200
    assert b'<div>Your city: <span id="city"></span></div>' in response.data
