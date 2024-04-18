from flight.domain.entities.flight import Flight
from flight.domain.validations.flight_validations import validate_date, validate_price
from flight.infrastructure.repositories.flight_repository import MongoDBFlightRepository

class RegisterFlight:
    def __init__(self, flight_repository: MongoDBFlightRepository):
        self.flight_repository = flight_repository

    def execute(self, city, state, date, price):
        if not validate_date(date):
            raise ValueError("Invalid date format, expected YYYY-MM-DD")
        if not validate_price(price):
            raise ValueError("Invalid price, must be a positive number")

        flight = Flight(city, state, date, price)
        self.flight_repository.save(flight)
        return flight
