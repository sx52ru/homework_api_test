
'''Configuration file
import pytest
import requests
import json

@pytest.fixture
def registered_user():
    """Фикстура для регистрации нового пользователя"""
    # Данные для регистрации
    registration_data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    # Отправка POST запроса на регистрацию
    response = requests.post(
        'https://reqres.in/api/register',
        data=json.dumps(registration_data),
        headers={'Content-Type': 'application/json'}
    )

    # Проверка статуса регистрации
    assert response.status_code == 200, "Регистрация не прошла успешно"

    # Получение токена из ответа
    registration_token = response.json()['token']

    # Создание словаря с данными зарегистрированного пользователя
    user_data = {
        'token': registration_token,
        'email': registration_data['email']
    }

    yield user_data  # Возврат данных пользователя

    # Очистка - удаление пользователя после теста
    requests.delete(
        f'https://reqres.in/api/users?token={registration_token}',
        headers={'Content-Type': 'application/json'}
    )

# Пример использования фикстуры в тесте
def test_login_with_registered_user(registered_user):
    """Проверка входа с зарегистрированным пользователем"""
    login_response = requests.post(
        'https://reqres.in/api/login',
        data=json.dumps({'email': registered_user['email']}),
        headers={'Content-Type': 'application/json'}
    )

    assert login_response.status_code == 200
    assert 'token' in login_response.json()'''

from dotenv import load_dotenv
import os

class Config:
    def __init__(self):
        pass

    BASE_URL = "https://reqres.in/api"
    CREATE_END_URL = "/register"
    LOGIN_END_URL = "/login"
    DELETE_END_URL = "/users/2"

    load_dotenv()
    USER_NAME = os.getenv('USER_NAME')
    PASSWORD = os.getenv('PASSWORD')
    EMAIL = os.getenv('EMAIL')
    X_API_KEY = os.getenv('X_API_KEY')

    HEADERS = {'Content-Type': 'application/json', 'x-api-key': X_API_KEY}



