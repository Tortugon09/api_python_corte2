from flask import Blueprint, jsonify, request
from trip.application.usecases.get_user_trips import GetUserTrips
from trip.infrastructure.repositories.trip_repository import TripRepository

get_user_trips_blueprint = Blueprint('get_user_trips', __name__)

def initialize_endpoints(repository):
    get_user_trips_usecase = GetUserTrips(trip_repository=repository)

    @get_user_trips_blueprint.route('/user_trips/<user_id>', methods=['GET'])
    def get_user_trips(user_id):
        try:
            trips = get_user_trips_usecase.execute(user_id)
            return jsonify([trip.serialize() for trip in trips]), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

