# класс для описания пользователя

class User:

    def __init__(self, user_id:int=None, email:str='', first_name:str = '', last_name:str='', avatar:str=''):
        self.user_id = user_id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.avatar = avatar

