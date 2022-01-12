from fixtures import *


def test_employee_single(client, mock_my_employee, mock_get_sqlalchemy):
    mock_get_sqlalchemy.get.return_value = mock_my_employee
    response = client.get('/api/v1/employees/1')

    assert "test@test.com" in str(response.data)
