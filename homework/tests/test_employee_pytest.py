from employee import Employee
# from fixtures import *
# import pytest
# import requests_mock
# import requests


def test_apply_raise():
    user = Employee('Olha', 'Knysh', 2000)
    user.apply_raise()
    assert user.pay == 2100


# def test_monthly_schedule(mocker):
#     # requests_mock.get(
#     #     "http://company.com/Abc/July", text="data_schedule", status_code=200
#     # )
#     user = Employee('Solka', 'Abc', 1000)
#     # assert user.monthly_schedule('July') == "data_schedule"
#     mocker.return_value.ok = False
#     mocker.return_value.text = 'data monthly schedule for July'
#     assert user.monthly_schedule('July') == 'Bad Response!'
