from user.domain.entities.user import User
from user.domain.validations.user_validations import validate_email
from user.infrastructure.repositories.user_repository import MongoDBUserRepository

class RegisterUser:
    def __init__(self, user_repository: MongoDBUserRepository):
        self.user_repository = user_repository

    def execute(self, name, email, password):
        if not validate_email(email):
            raise ValueError("Invalid email format")

        user = User(name, email, password)
        self.user_repository.save(user)