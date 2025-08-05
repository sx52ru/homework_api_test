from utils.config import Config
import requests
import json


def test_create_user(prepare_user_account):
    response = requests.post(url=Config.BASE_URL + Config.CREATE_END_URL,
                             data=json.dumps({'email': prepare_user_account.user_email,
                                              'password': prepare_user_account.user_pass}),
                             headers=Config.HEADERS)
    assert response.status_code == 200
    assert response.json()['token'] == 'QpwL5tke4Pnpja7X4'
    assert response.json()['id'] == 4

    #user =
    # = UserAccount.create_user(user)
