import pytest

from apps.cars.models import Car
from tests.fixtures.cars import CarFactory, CarModelFactory, CarBrandFactory


@pytest.mark.django_db()
def test_car_photos():
    brand = CarBrandFactory(name='Audi')
    car = CarFactory(model=CarModelFactory(name='A4', brand=brand), extra_title='Best deal')

    assert Car.objects.count() == 1
    assert car.title == 'Audi Best deal'
    assert str(car) == 'Audi Best deal'

    car.extra_title = None
    assert car.title == 'Audi '
