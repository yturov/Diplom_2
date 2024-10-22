import random
import string


def generated_data_user():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    name = generate_random_string(10)
    email = generate_random_string(10) + '@yandex.ru'
    password = generate_random_string(10)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    return payload
