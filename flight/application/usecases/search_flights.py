from flight.infrastructure.repositories.flight_repository import MongoDBFlightRepository

class SearchFlights:
    def __init__(self, flight_repository: MongoDBFlightRepository):
        self.flight_repository = flight_repository

    def execute(self):
        return self.flight_repository.find_all()

    def execute_by_city(self, city):
        return self.flight_repository.find_by_city(city)

    def execute_by_state(self, state):
        return self.flight_repository.find_by_state(state)
