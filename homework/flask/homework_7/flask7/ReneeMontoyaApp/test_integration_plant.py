from fixtures import *


def test_plant_get(client):
    response = client.get('/api/v1/plants')

    assert response.status_code == 200


def test_plant_post(client, plant_to_post):
    response = client.post('/api/v1/plants', json=plant_to_post)

    assert response.status_code == 200


def test_plant_put(client, plant_to_put):
    get_response = client.get('/api/v1/plants')
    if len(get_response.json) > 0 and get_response.json[-1].get('id') is not None:
        value1_node = get_response.json[-1].get('id')
        response = client.put('/api/v1/plants/' + str(value1_node), json=plant_to_put)

        assert "PutLocation" in str(response.data)
        assert "PutTest" in str(response.data)
        assert response.status_code == 200


def test_plant_delete(client):
    get_response = client.get('/api/v1/plants')
    if len(get_response.json) > 0 and get_response.json[-1].get('id') is not None:
        value1_node = get_response.json[-1].get('id')
        response = client.delete('/api/v1/plants/' + str(value1_node))

        assert response.status_code == 204
