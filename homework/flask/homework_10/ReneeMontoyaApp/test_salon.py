from fixtures import *


def test_salon_single(client, mock_my_salon, mock_get_sqlalchemy):
    mock_get_sqlalchemy.get.return_value = mock_my_salon
    response = client.get('/api/v1/salons/1')

    assert 'Testovy' in str(response.data)
    assert 'Test' in str(response.data)
