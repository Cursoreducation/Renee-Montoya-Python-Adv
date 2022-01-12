from fixtures import *


def test_plant_single(client, mock_my_plant, mock_get_sqlalchemy):
    mock_get_sqlalchemy.get.return_value = mock_my_plant
    response = client.get('/api/v1/plants/100')

    assert "Kiev" in str(response.data)
    assert "Test" in str(response.data)
