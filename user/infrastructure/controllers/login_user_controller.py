from flask import Blueprint, request, jsonify
from user.application.usecases.login_user import LoginUser
from user.infrastructure.repositories.user_repository import MongoDBUserRepository
from user.infrastructure.services.user_services import UserServices
from user.domain.validations.user_validations import validate_email

login_user_blueprint = Blueprint('login_user', __name__)

def initialize_endpoints(repository):
    login_user_usecase = LoginUser(user_repository=repository)
    user_services = UserServices(repository, secret_key="YOUR_SECRET_KEY")

    @login_user_blueprint.route('/login', methods=['POST'])
    def login_user():
        data = request.get_json()

        if not data or 'email' not in data or 'password' not in data:
            return jsonify({"error": "Email and password are required"}), 400

        email = data.get('email')
        password = data.get('password')

        if len(email) > 255 or len(email) < 6 or not validate_email(email):
            return jsonify({"error": "Invalid email format or length"}), 400
        if len(password) > 12 or len(password) < 6:
            return jsonify({"error": "Invalid password length"}), 400
        
        user = login_user_usecase.execute(email, password)
        if user:
            return jsonify({
                "message": "Login successful",
                "user": user.name,
                "user_id": user.id 
            }), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 401