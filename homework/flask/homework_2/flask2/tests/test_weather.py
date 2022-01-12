import pytest
from tests.weather_info import WeatherInfo


def test_weather(mocker, fake_info, client):
    res = mocker.Mock()
    res.json = mocker.Mock(return_value=fake_info)
    res.status_code = 200
    mocker.patch("routes.weather.requests.get", return_value=res)

    response = client.get("/weather?city=Kiev")

    assert WeatherInfo.from_dict(response.json) == \
           WeatherInfo.from_dict(fake_info)


def test_multiweather(mocker, multi_fake_info, client):
    res = mocker.Mock()
    res.json = mocker.Mock(return_value=multi_fake_info)
    res.status_code = 200
    mocker.patch("routes.weather.requests.get", return_value=res)

    response = client.get("/weather?city=Kiev%20Lviv")

    assert WeatherInfo.from_dict(response.json[0][0]) == \
           WeatherInfo.from_dict(multi_fake_info[0])
    assert WeatherInfo.from_dict(response.json[0][1]) == \
           WeatherInfo.from_dict(multi_fake_info[1])
