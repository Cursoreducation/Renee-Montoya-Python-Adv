from fixtures import *


def test_menu_post(client, menuitem_data):
    response = client.post('/api/v1/menu-items', json=menuitem_data)

    assert response.status_code == 200


def test_menu_get(client):
    response = client.get('/api/v1/menu-items')

    assert response.status_code == 200
    assert 'menu' in str(response.data)


def test_menu_put(client, menuitem_put_data):
    get_response = client.get('/api/v1/menu-items')
    if len(get_response.json) > 0 and get_response.json[-1].get('id') is not None:
        value1_node = get_response.json[-1].get('id')
        response = client.put('/api/v1/menu-items/' + str(value1_node), json=menuitem_put_data)

        assert response.status_code == 200

def test_menu_delete(client):
    get_response = client.get('/api/v1/menu-items')
    if len(get_response.json) > 0 and get_response.json[-1].get('id') is not None:
        value1_node = get_response.json[-1].get('id')
        response = client.delete('/api/v1/menu-items/' + str(value1_node))

        assert response.status_code == 204
