from flask import Blueprint, jsonify, request
from flight.application.usecases.search_flights import SearchFlights
from flight.infrastructure.repositories.flight_repository import MongoDBFlightRepository

search_flights_blueprint = Blueprint('search_flights', __name__)

def initialize_endpoints(repository):
    search_flights_usecase = SearchFlights(flight_repository=repository)

    @search_flights_blueprint.route('/all', methods=['GET'])
    def get_all_flights():
        flights = search_flights_usecase.execute()
        flights_data = [{
            'city': flight.city,
            'state': flight.state,
            'date': flight.date,
            'price': flight.price,
            'id': flight.id
        } for flight in flights]
        return jsonify(flights_data)
    
    @search_flights_blueprint.route('/by_city', methods=['GET'])
    def get_flights_by_city():
        city = request.args.get('city')
        flights = search_flights_usecase.execute_by_city(city)
        flights_data = [{
            'city': flight.city,
            'state': flight.state,
            'date': flight.date,
            'price': flight.price,
            'id': flight.id
        } for flight in flights]
        return jsonify(flights_data)

    @search_flights_blueprint.route('/by_state', methods=['GET'])
    def get_flights_by_state():
        state = request.args.get('state')
        flights = search_flights_usecase.execute_by_state(state)
        flights_data = [{
            'city': flight.city,
            'state': flight.state,
            'date': flight.date,
            'price': flight.price,
            'id': flight.id
        } for flight in flights]
        return jsonify(flights_data)
