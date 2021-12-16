import pytest
from rest_framework.reverse import reverse

from apps.orders.models import Order
from tests.fixtures.cars import CarFactory, OrderFactory


@pytest.mark.django_db
def test_order_create(client):
    car = CarFactory()
    data = {
        'first_name': 'Dead',
        'last_name': 'Rabbit',
        'email': 'big_lag@gmail.com',
        'car_id': car.id,
        'phone': '28947842942',
    }

    assert Order.objects.count() == 0

    resp = client.post(
        path=reverse('orders:create'),
        data=data
    )
    assert resp.status_code == 201
    orders = Order.objects.all()
    assert len(orders) == 1
    assert orders[0].first_name == 'Dead'
    assert orders[0].last_name == 'Rabbit'
    assert orders[0].email == 'big_lag@gmail.com'
    assert orders[0].phone == '28947842942'
    assert orders[0].car_id == car.id


@pytest.mark.django_db
def test_order_create_unique(client):
    car = CarFactory()
    OrderFactory(email='pupsik228@gmail.com', car=car)

    data = {
        'first_name': 'Dead',
        'last_name': 'Rabbit',
        'email': 'pupsik228@gmail.com',
        'car': car.id,
        'phone': '28947842942',
    }

    resp = client.post(
        path=reverse('orders:create'),
        data=data
    )
    assert resp.status_code == 400
    assert Order.objects.count() == 1
