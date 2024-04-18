from flask import Blueprint, request, jsonify
from user.application.usecases.register_user import RegisterUser
from user.infrastructure.repositories.user_repository import MongoDBUserRepository
from user.infrastructure.services.user_services import UserServices
from user.domain.validations.user_validations import validate_email
from user.domain.validations.user_validations import validate_name

create_user_blueprint = Blueprint('create_user', __name__)

def initialize_endpoints(repository):
    register_user_usecase = RegisterUser(user_repository=repository)
    user_services = UserServices(repository, secret_key="YOUR_SECRET_KEY")
    
    @create_user_blueprint.route('/register', methods=['POST'])
    def register_user():
        data = request.get_json()

        if not data or not all(key in data for key in ['name', 'email', 'password']):
            return jsonify({"error": "Name, email, and password are required"}), 400

        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        if len(email) > 255 or len(email) < 6 or not validate_email(email):
            return jsonify({"error": "Invalid email format or length"}), 400
        if len(name) > 50 or len(name) < 6 or not validate_name(name):
            return jsonify({"error": "Invalid name format or length"}), 400
        if len(password) > 12 or len(password) < 6:
            return jsonify({"error": "Invalid password length"}), 400

        if repository.find_by_email(email):
            return jsonify({"error": "Email already registered"}), 400

        try:
            register_user_usecase.execute(name, email, password)
            user = repository.find_by_email(email)
            if user:
                token = user_services.generate_token(user.email)
                return jsonify({"message": "User registered successfully", "token": token}), 201
            else:
                return jsonify({"error": "User not found after registration"}), 404
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
