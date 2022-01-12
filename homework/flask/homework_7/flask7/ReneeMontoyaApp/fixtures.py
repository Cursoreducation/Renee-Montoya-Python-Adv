import pytest
from app import app, db
from models import *


@pytest.fixture
def client():
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://flask:flask@db:3306/flask"
    app.config.testing = True
    client = app.test_client()

    with app.app_context():
        db.create_all()
        db.session.commit()
        yield client


@pytest.fixture
def mock_my_plant():
    return Plant(id=1, location="Kiev", name="Test")


@pytest.fixture
def mock_my_employee():
    return Employee(id=1, name="Test", email="test@test.com", department_type="plant", department_id=1)


@pytest.fixture
def mock_my_salon():
    return Salon(id=1, name="Test", director_id=1, city="Kiev", address="Testovy")


@pytest.fixture
def mock_get_sqlalchemy(mocker):
    mock = mocker.patch("flask_sqlalchemy._QueryProperty.__get__").return_value = mocker.Mock()
    return mock


@pytest.fixture
def plant_to_post():
    yield {"id": 1, "location": "Kiev", "name": "Test"}


@pytest.fixture
def employee_to_post():
    yield {"id": 1, "name": "Test", "email": "test@test.com", "department_type": "Test", "department_id": 1}


@pytest.fixture
def salon_to_post():
    yield {"id": 1, "director_id": 1, "name": "Test", "city": "Kiev", "address": "Testovy"}


@pytest.fixture
def plant_to_put():
    yield {"location": "PutLocation", "name": "PutTest"}


@pytest.fixture
def employee_to_put():
    yield {"name": "PutTest", "email": "puttest@test.com"}


@pytest.fixture
def salon_to_put():
    yield {"name": "PutTest", "city": "PutCity", "address": "PutTestovy"}
