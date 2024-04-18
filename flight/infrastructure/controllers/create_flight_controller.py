from flask import Blueprint, request, jsonify
from flight.application.usecases.register_flight import RegisterFlight
from flight.infrastructure.repositories.flight_repository import MongoDBFlightRepository

create_flight_blueprint = Blueprint('create_flight', __name__)

def initialize_endpoints(repository):
    register_flight_usecase = RegisterFlight(flight_repository=repository)

    @create_flight_blueprint.route('/register', methods=['POST'])
    def create_flight():
        data = request.get_json()

        # Validate the presence of all required fields
        if not data or not all(key in data for key in ['city', 'state', 'date', 'price']):
            return jsonify({"error": "All fields (city, state, date, price) are required"}), 400

        city = data.get('city')
        state = data.get('state')
        date = data.get('date')
        price = data.get('price')

        try:
            flight = register_flight_usecase.execute(city, state, date, price)
            return jsonify({"message": "Flight registered successfully", "flight_id": flight.id}), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
