from flask import request, jsonify
from user.infrastructure.services.user_services import UserServices
from functools import wraps

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403

        try:
            user_services = UserServices(None, secret_key="YOUR_SECRET_KEY")
            user_id = user_services.decode_token(token)
            if not user_id:
                raise ValueError("Invalid or expired token")
        except Exception as e:
            return jsonify({'message': str(e)}), 403

        return f(*args, **kwargs)

    return decorated
