# фикстура подготовки данных пользователя

import pytest
from models.account import UserAccount
from utils.config import Config


@pytest.fixture(scope="session")
def prepare_user_account():
    return UserAccount(Config.USER_NAME, Config.PASSWORD, Config.EMAIL)







