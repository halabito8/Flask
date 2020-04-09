from flask_login import UserMixin

from .conexionDB import get_user_by_id

class UserData:
    def __init__(self,  username, password, user_id):
        self.username = username
        self.password = password
        self.user_id = user_id

class UserModel(UserMixin):
    def __init__(self, user_data):
        self.user = user_data.username
        self.password = user_data.password
        self.id=user_data.user_id

    @staticmethod
    def query(user_id):
        results = get_user_by_id(user_id)
        user_data = UserData(
            username=results[0]['user'],
            password= results[0]['passwrd'],
            user_id=results[0]['user_id']
        )
        return UserModel(user_data)