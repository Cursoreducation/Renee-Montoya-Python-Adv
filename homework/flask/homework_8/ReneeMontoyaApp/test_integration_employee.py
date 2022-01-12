from fixtures import *


def test_employee_get(client):
    response = client.get('/api/v1/employees')

    assert response.status_code == 200


def test_employee_post(client, employee_to_post):
    response = client.post('/api/v1/employees', json=employee_to_post)

    assert response.status_code == 200


def test_employee_put(client, employee_to_put):
    get_response = client.get('/api/v1/employees')
    if len(get_response.json) > 0 and get_response.json[-1].get('id') is not None:
        value1_node = get_response.json[-1].get('id')
        response = client.put('/api/v1/employees/' + str(value1_node), json=employee_to_put)

        assert "PutTest" in str(response.data)
        assert "PutLocation" in str(response.data)
        assert response.status_code == 200


def test_employee_delete(client):
    get_response = client.get('/api/v1/employees')
    if len(get_response.json) > 0 and get_response.json[-1].get('id') is not None:
        value1_node = get_response.json[-1].get('id')
        response = client.delete('/api/v1/employees/' + str(value1_node))

        assert response.status_code == 204
