# конфигурационный файл
# переменные окружения

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



