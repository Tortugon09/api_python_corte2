from pymongo import MongoClient
from user.domain.entities.user import User

class MongoDBUserRepository:
    def __init__(self, connection_string, database_name):
        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]
        self.collection = self.db['users']

    def save(self, user: User):
        user_data = {
            'name': user.name,
            'email': user.email,
            'password': user.password
        }
        result = self.collection.insert_one(user_data)
        user.id = str(result.inserted_id) 
        
    def find_by_name(self, name):
        user_data = self.collection.find_one({'name': name})
        if user_data:
            return User(user_data['name'], user_data['email'], user_data['password'], str(user_data['_id']))
        return None

    def find_by_email(self, email):
        user_data = self.collection.find_one({'email': email})
        if user_data:
            return User(user_data['name'], user_data['email'], user_data['password'], str(user_data['_id']))
        return None