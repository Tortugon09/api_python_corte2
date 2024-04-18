from flask import Blueprint
from user.infrastructure.controllers.create_user_controller import create_user_blueprint, initialize_endpoints as create_user_endpoints
from user.infrastructure.controllers.login_user_controller import login_user_blueprint, initialize_endpoints as login_user_endpoints
from user.infrastructure.repositories.user_repository import MongoDBUserRepository 

user_router = Blueprint('user_router', __name__)

def initialize_endpoints(repository):
    create_user_endpoints(repository)
    login_user_endpoints(repository)

initialize_endpoints(MongoDBUserRepository(connection_string='mongodb://localhost:27017/', database_name='vuelos'))

user_router.register_blueprint(create_user_blueprint, url_prefix='/api/users')
user_router.register_blueprint(login_user_blueprint, url_prefix='/api/users')
