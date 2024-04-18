from trip.infrastructure.repositories.trip_repository import TripRepository

class GetUserTrips:
    def __init__(self, trip_repository: TripRepository):
        self.trip_repository = trip_repository

    def execute(self, user_id):
        return self.trip_repository.find_by_user_id(user_id)
