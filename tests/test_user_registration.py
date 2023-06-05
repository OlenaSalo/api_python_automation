import faker
import requests
import json

from src.condition import status_code, body
from src.services import UserApiService
from hamcrest import has_length, greater_than


def test_can_register_user_valid_credentials(faker):
    user = {"username": faker.name(), "password": "123456", "email": "demo@gmail.com"}

    response = UserApiService().create_user(user)

    response.should_have(status_code(200))
    response.should_have(body("$.id", has_length(greater_than(0))))
    # assert len(response.field('id')) > 0


def test_can_not_register_user_with_same_credentials_twice(faker):
    user = {"username": faker.name(), "password": "123456", "email": "demo@gmail.com"}

    response = UserApiService().create_user(user)

    response.should_have(status_code(200))

    response = UserApiService().create_user(user)

    response.should_have(status_code(500))
    # assert response.status_code(500)