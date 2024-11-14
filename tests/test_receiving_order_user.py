import allure
import requests
from data import Url, Message, Ingredients


class TestReceivingOrdersUser:
    @allure.title("Получения заказа авторизованным пользователем")
    def test_get_order_auth_user(self, create_user):
        response, payload = create_user
        token = response.json()['accessToken']
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        ingredients = {"ingredients": [Ingredients.KRATOR_BUN, Ingredients.GALAKTIK_SOUSE, Ingredients.CHEES_FILLING]}
        requests.post(Url.CREATE_ORDER, data=ingredients, headers=headers)
        answer = requests.get(Url.GET_ORDER, headers=headers)
        assert answer.status_code == 200
        assert Message.SUCCESS_TRUE in answer.text

    @allure.title("Получение заказа неавторизованным пользователем")
    def test_get_order_no_auth_user(self):
        answer = requests.get(Url.GET_ORDER)
        assert answer.status_code == 401
        assert Message.ORDER_NO_AUTHORIZED in answer.text
