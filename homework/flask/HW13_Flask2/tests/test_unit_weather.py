import pytest
import requests


def test_url_weather(requests_mock, client):
    json = {'location': {'name': 'Kiev'}}
    requests_mock.get('http://api.weatherapi.com/v1/current.json', json=json)
    response = client.get('/weather?city=Kiev')
    assert response.status == '200 OK'
    assert json == response.json


def test_url_weathers(requests_mock, client):
    json = {'location': {'name': 'Kiev'}}
    requests_mock.get('http://api.weatherapi.com/v1/current.json', json=json)
    response = client.get('/weathers?city=Lviv,Kiev')
    assert response.status == '200 OK'
    assert {'Lviv': json, 'Kiev': json} == response.json
