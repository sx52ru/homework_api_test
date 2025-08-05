import requests
import json

from utils.config import Config

def test_login_user(prepare_user_account):
    response = requests.post(url=Config.BASE_URL + Config.LOGIN_END_URL,
                             data=json.dumps({'email': prepare_user_account.user_email,
                                              'password': prepare_user_account.user_pass}),
                             headers=Config.HEADERS)
    assert response.status_code == 200, "Авторизация не удалась"
    assert response.json()['token'] == 'QpwL5tke4Pnpja7X4', "Авторизация не удалась"



