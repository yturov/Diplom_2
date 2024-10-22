import allure
import requests
from data import Url, Message, Ingredients


class TestCreateOrder:
    @allure.title("Создание заказа с авторизацией и ингредиентами")
    def test_create_order_auth_user_ingredients(self, create_user):
        response, payload = create_user
        requests.post(Url.LOGIN_USER, data=payload)
        ingredients = {"ingredients": [Ingredients.KRATOR_BUN, Ingredients.GALAKTIK_SOUSE, Ingredients.CHEES_FILLING]}
        answer = requests.post(Url.CREATE_ORDER, data=ingredients)

        assert answer.status_code == 200
        assert Message.SUCCESS_TRUE in answer.text
        assert answer.json()['order']['number'] is not None

    @allure.title("Создание заказа без авторизации и с ингредиентами")
    def test_create_order_not_auth_user_ingredients(self):
        ingredients = {"ingredients": [Ingredients.KRATOR_BUN, Ingredients.GALAKTIK_SOUSE, Ingredients.CHEES_FILLING]}
        answer = requests.post(Url.CREATE_ORDER, data=ingredients)
        assert answer.status_code == 200
        assert Message.SUCCESS_TRUE in answer.text

    @allure.title("Создание заказа с авторизацией и без ингредиентов")
    def test_create_order_auth_user_no_ingredients(self, create_user):
        response, payload = create_user
        requests.post(Url.LOGIN_USER, data=payload)
        ingredients = {"ingredients": ['']}
        answer = requests.post(Url.CREATE_ORDER, data=ingredients)
        assert answer.status_code == 400
        assert Message.NO_INGREDIENT in answer.text

    @allure.title("Создание заказа без авторизации и неверным хешем ингредиентов")
    def test_create_order_no_auth_user_bad_hash(self):
        ingredients = {"ingredients": [Ingredients.BAD_HASH, Ingredients.GALAKTIK_SOUSE, Ingredients.CHEES_FILLING]}
        answer = requests.post(Url.CREATE_ORDER, data=ingredients)
        assert answer.status_code == 500
        assert Message.BAD_HASH_INGREDIENTS in answer.text
