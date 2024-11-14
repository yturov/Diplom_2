import allure
import requests
from data import Url, Message
from helpers import generated_data_user


class TestLoginUser:
    @allure.title("Вход под существующим пользователем")
    def test_login_true_user(self, create_user):
        response, payload = create_user
        payload_no_field_name = dict(payload)
        del payload_no_field_name['name']
        answer = requests.post(Url.LOGIN_USER, data=payload_no_field_name)
        assert answer.status_code == 200
        assert Message.SUCCESS_TRUE in answer.text

    @allure.title("Вход с неверным логином и паролем")
    def test_login_with_incorrect_login_and_password(self):
        payload = generated_data_user()
        del payload['name']
        answer = requests.post(Url.LOGIN_USER, data=payload)

        assert answer.status_code == 401
        assert Message.INCORRECT_LOGIN_AND_PASSWORD in answer.text

