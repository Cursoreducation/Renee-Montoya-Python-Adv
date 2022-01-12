from fixtures import *


def test_salon_get(client):
    response = client.get('/api/v1/salons')

    assert response.status_code == 200


def test_salon_post(client, salon_to_post):
    response = client.post('/api/v1/salons', json=salon_to_post)

    assert response.status_code == 200


def test_salon_put(client, salon_to_put):
    get_response = client.get('/api/v1/salons')
    if len(get_response.json) > 0 and get_response.json[-1].get('id') is not None:
        value1_node = get_response.json[-1].get('id')
        response = client.put('/api/v1/salons/' + str(value1_node), json=salon_to_put)

        assert "PutTest" in str(response.data)
        assert response.status_code == 200


def test_salon_delete(client):
    get_response = client.get('/api/v1/salons')
    if len(get_response.json) > 0 and get_response.json[-1].get('id') is not None:
        value1_node = get_response.json[-1].get('id')
        response = client.delete('/api/v1/salons/' + str(value1_node))

        assert response.status_code == 204
