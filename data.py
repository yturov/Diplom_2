class Url:
    URL = "https://stellarburgers.nomoreparties.site"
    CREATE_USER = f"{URL}/api/auth/register"
    DELETE_USER = f"{URL}/api/auth/user"
    LOGIN_USER = f"{URL}/api/auth/login"
    UPDATE_DATA = f"{URL}/api/auth/user"
    CREATE_ORDER = f"{URL}/api/orders"
    GET_ORDER = f"{URL}/api/orders"


class Message:
    SUCCESS_TRUE = '"success":true'
    SUCCESS_FALSE = '"success":false,"message":"User already exists"'
    NO_EMAIL_OR_PASSWORD_OR_NAME = '"success":false,"message":"Email, password and name are required fields"'
    INCORRECT_LOGIN_AND_PASSWORD = '"success":false,"message":"email or password are incorrect"'
    NO_AUTHORIZED = '"success":false,"message":"You should be authorised"'
    MATCH_VALUE = '"success":false,"message":"User with such email already exists"'
    NO_INGREDIENT = '"success":false,"message":"Ingredient ids must be provided"'
    BAD_HASH_INGREDIENTS = "Internal Server Error"
    ORDER_NO_AUTHORIZED = '"success":false,"message":"You should be authorised"'


class Ingredients:
    KRATOR_BUN = "61c0c5a71d1f82001bdaaa74"
    CHEES_FILLING = '61c0c5a71d1f82001bdaaa6c'
    GALAKTIK_SOUSE = '61c0c5a71d1f82001bdaaa7a'
    BAD_HASH = '77c7c7a77d7f77001bdaaa7'