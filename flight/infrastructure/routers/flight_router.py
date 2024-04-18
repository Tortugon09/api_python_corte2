from flask import Blueprint
from flight.infrastructure.controllers.create_flight_controller import create_flight_blueprint, initialize_endpoints as create_flight_endpoints
from flight.infrastructure.controllers.search_flights_controller import search_flights_blueprint, initialize_endpoints as search_flights_endpoints
from flight.infrastructure.repositories.flight_repository import MongoDBFlightRepository 

flight_router = Blueprint('flight_router', __name__)

def initialize_endpoints(repository):
    create_flight_endpoints(repository)
    search_flights_endpoints(repository)

repository = MongoDBFlightRepository(connection_string='mongodb://localhost:27017/', database_name='vuelos')
initialize_endpoints(repository)

flight_router.register_blueprint(create_flight_blueprint, url_prefix='/api/flights')
flight_router.register_blueprint(search_flights_blueprint, url_prefix='/api/flights')
