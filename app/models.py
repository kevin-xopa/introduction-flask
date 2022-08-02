from webbrowser import get
from flask_login import UserMixin
from .firestore_service import get_user


class UserData:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class UserModel(UserMixin):
    def __init__(self, user_data):
        """
            Create a new UserModel instance
            Args: user_data: UserData
        """
        self.id = user_data.username
        self.password = user_data.password

    @staticmethod
    def query(user_id):
        user = get_user(user_id)
        user_date = UserData(
            username=user.id,
            password=user.to_dict()["password"]
        )
        return UserModel(user_date)
