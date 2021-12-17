import pytest

from apps.cars.models import Car
from tests.fixtures.cars import CarFactory, CarModelFactory, CarBrandFactory
from tests.fixtures.photos import PhotoFactory


@pytest.mark.django_db()
def test_car_title():
    brand = CarBrandFactory(name='Audi')
    car = CarFactory(model=CarModelFactory(name='A4', brand=brand), extra_title='Best deal')

    assert Car.objects.count() == 1
    assert car.title == 'Audi Best deal'
    assert str(car) == 'Audi Best deal'

    car.extra_title = None
    assert car.title == 'Audi '


@pytest.mark.django_db()
def test_car_model_title():
    brand = CarBrandFactory(name='Audi')
    CarFactory(model=CarModelFactory(name='A4', brand=brand), extra_title='Best deal')

    car = Car.objects.last()
    assert car.model_brand_title == 'Audi A4'


@pytest.mark.django_db()
def test_car_model_title():
    brand = CarBrandFactory(name='Audi')
    car = CarFactory(model=CarModelFactory(name='A4', brand=brand), extra_title='Best deal')

    PhotoFactory(car=car, position=2)
    PhotoFactory(car=car, position=3)
    PhotoFactory(car=car, position=1)

    photos = car.photos.all()
    assert [p.position for p in photos] == [1, 2, 3]
