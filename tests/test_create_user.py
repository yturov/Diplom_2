import allure
import requests
from data import Url, Message
from helpers import generated_data_user


class TestCreateUser:
    @allure.title('Создание уникального пользователя')
    def test_create_unique_user(self, create_user):
        response, payload = create_user
        assert response.status_code == 200
        assert Message.SUCCESS_TRUE in response.text

    @allure.title("Cоздание пользователя, который уже зарегистрирован")
    def test_create_identical_user(self, create_user):
        response, payload = create_user
        answer = requests.post(Url.CREATE_USER, data=payload)
        assert answer.status_code == 403
        assert Message.SUCCESS_FALSE in answer.text

    @allure.title("Создание пользователя без почты")
    def test_create_user_no_email(self):
        payload = generated_data_user()
        payload['email'] = ''
        answer = requests.post(Url.CREATE_USER, data=payload)
        assert answer.status_code == 403
        assert Message.NO_EMAIL_OR_PASSWORD_OR_NAME in answer.text

    @allure.title("Создание пользователя без имени")
    def test_create_user_no_name(self):
        payload = generated_data_user()
        payload['name'] = ''
        answer = requests.post(Url.CREATE_USER, data=payload)
        assert answer.status_code == 403
        assert Message.NO_EMAIL_OR_PASSWORD_OR_NAME in answer.text

    @allure.title("Создание пользователя без пароля")
    def test_create_user_no_password(self):
        payload = generated_data_user()
        payload['password'] = ''
        answer = requests.post(Url.CREATE_USER, data=payload)
        assert answer.status_code == 403
        assert Message.NO_EMAIL_OR_PASSWORD_OR_NAME in answer.text
