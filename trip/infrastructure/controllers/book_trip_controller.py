from flask import Blueprint, request, jsonify
from trip.application.usecases.book_trip import BookTrip
from trip.infrastructure.repositories.trip_repository import TripRepository

book_trip_blueprint = Blueprint('book_trip', __name__)

def initialize_endpoints(repository):
    book_trip_usecase = BookTrip(trip_repository=repository)

    @book_trip_blueprint.route('/book', methods=['POST'])
    def book_trip():
        data = request.get_json()

        # Validate the presence of all required fields
        if not data or not all(key in data for key in ['user_id', 'flight_id', 'trip_type', 'departure_date', 'luggage_type', 'seat_count', 'passenger_names'] + (['return_date'] if data.get('trip_type') == 'round' else [])):
            return jsonify({"error": "Missing required fields"}), 400

        user_id = data['user_id']
        flight_id = data['flight_id']
        trip_type = data['trip_type']
        departure_date = data['departure_date']
        return_date = data.get('return_date', None)
        luggage_type = data['luggage_type']
        seat_count = data['seat_count']
        passenger_names = data['passenger_names']

        try:
            result = book_trip_usecase.execute(user_id, flight_id, trip_type, departure_date, return_date, luggage_type, seat_count, passenger_names)
            return jsonify(result), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400