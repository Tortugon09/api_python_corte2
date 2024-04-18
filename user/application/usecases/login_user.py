from user.infrastructure.repositories.user_repository import MongoDBUserRepository

class LoginUser:
    def __init__(self, user_repository: MongoDBUserRepository):
        self.user_repository = user_repository

    def execute(self, email, password):
        user = self.user_repository.find_by_email(email)
        if user and user.check_password(password):
            return user
        return None