import pytest
import requests
from helpers import generated_data_user
from data import Url


@pytest.fixture(scope='function')
def create_user():
    payload = generated_data_user()
    response = requests.post(Url.CREATE_USER, data=payload)
    token = response.json()['accessToken']
    headers = {"Content-type": "application/json", "Authorization": f'{token}'}
    yield response, payload
    requests.delete(Url.DELETE_USER, headers=headers)
