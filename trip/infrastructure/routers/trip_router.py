from flask import Blueprint
from trip.infrastructure.controllers.book_trip_controller import book_trip_blueprint, initialize_endpoints as book_trip_endpoints
from trip.infrastructure.controllers.get_user_trips_controller import get_user_trips_blueprint, initialize_endpoints as get_user_trips_endpoints
from trip.infrastructure.repositories.trip_repository import TripRepository

trip_router = Blueprint('trip_router', __name__)

def initialize_endpoints(repository):
    book_trip_endpoints(repository)
    get_user_trips_endpoints(repository)

repository = TripRepository(connection_string='mongodb://localhost:27017/', database_name='vuelos')
initialize_endpoints(repository)

trip_router.register_blueprint(book_trip_blueprint, url_prefix='/api/trips')
trip_router.register_blueprint(get_user_trips_blueprint, url_prefix='/api/trips')