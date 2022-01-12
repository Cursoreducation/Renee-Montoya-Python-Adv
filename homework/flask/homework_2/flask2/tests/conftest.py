import pytest
from app import app
import json
from flask import template_rendered


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


@pytest.fixture
def fake_info():
    with open("tests/resources/weather.json") as f:
        return json.load(f)


@pytest.fixture
def multi_fake_info():
    with open("tests/resources/multiweather.json") as f:
        return json.load(f)
