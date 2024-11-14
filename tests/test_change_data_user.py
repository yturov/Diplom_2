import allure
import requests
from data import Url, Message


class TestChangeDataUser:

    @allure.title("Изменение name у авторизованного пользователя")
    def test_changes_name_authorized_user(self, create_user):
        response, payload = create_user
        token = response.json()['accessToken']
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        changes_name = 'change77777' + payload["name"]
        new_name = {"name": changes_name}
        answer = requests.patch(Url.UPDATE_DATA, json=new_name, headers=headers)
        assert answer.status_code == 200
        assert answer.json()['user']['name'] == new_name['name']
        assert Message.SUCCESS_TRUE in answer.text

    @allure.title("Изменение email у авторизованного пользователя")
    def test_changes_email_authorized_user(self, create_user):
        response, payload = create_user
        token = response.json()['accessToken']
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        changes_email = 'change888888' + payload["email"]
        new_email = {"email": changes_email}
        answer = requests.patch(Url.UPDATE_DATA, json=new_email, headers=headers)
        assert answer.status_code == 200
        assert answer.json()['user']['email'] == new_email['email']
        assert Message.SUCCESS_TRUE in answer.text

    @allure.title("Изменение password у авторизованного пользователя")
    def test_changes_password_authorized_user(self, create_user):
        response, payload = create_user
        token = response.json()['accessToken']
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        changes_password = 'change4' + payload["password"]
        new_password = {"password": changes_password}
        answer = requests.patch(Url.UPDATE_DATA, json=new_password, headers=headers)

        assert answer.status_code == 200
        assert Message.SUCCESS_TRUE in answer.text

    @allure.title("Изменение email у неавторизованного пользователя")
    def test_changes_email_no_authorized_user(self, create_user):
        response, payload = create_user
        requests.post(Url.CREATE_USER, data=payload)
        headers = {"Content-type": "application/json"}
        changes_email = 'change888888' + payload["email"]
        new_email = {"email": changes_email}
        answer = requests.patch(Url.UPDATE_DATA, json=new_email, headers=headers)

        assert answer.status_code == 401
        assert Message.NO_AUTHORIZED in answer.text

    @allure.title("Изменение email, на уже существующие в системе у авторизованного пользователя")
    def test_changes_email_error_403(self, create_user):
        response, payload = create_user
        token = response.json()['accessToken']
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        new_email = {"email": "yuri_turov_13_777@yandex.ru"}
        answer = requests.patch(Url.UPDATE_DATA, json=new_email, headers=headers)
        assert answer.status_code == 403
        assert Message.MATCH_VALUE in answer.text
