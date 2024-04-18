from trip.infrastructure.repositories.trip_repository import TripRepository
from trip.domain.validations.trip_validations import validate_dates, validate_luggage
from trip.domain.entities.trip import Trip

class BookTrip:
    def __init__(self, trip_repository: TripRepository):
        self.trip_repository = trip_repository

    def execute(self, user_id, flight_id, trip_type, departure_date, return_date, luggage_type, seat_count, passenger_names):
        if not validate_dates(departure_date, return_date if trip_type == 'round' else None):
            raise ValueError("Invalid dates")
        if not validate_luggage(luggage_type):
            raise ValueError("Invalid luggage type")
        if len(passenger_names) != seat_count:
            raise ValueError("Number of passenger names must match seat count")

        # Obtain base price of flight
        base_price = self.trip_repository.get_flight_price(flight_id)
        if not base_price:
            raise ValueError("Flight not found or invalid flight ID")

        # Luggage cost per seat
        luggage_cost_per_seat = {'basic': 0, 'medium': 300, 'premium': 500}[luggage_type]

        # Calculate total base price depending on the trip type
        if trip_type == 'round':
            base_price *= 2  # Price is doubled for round trips

        # Total cost calculation includes the base price, luggage cost, and number of seats
        total_cost = (base_price + luggage_cost_per_seat) * seat_count

        trip = Trip(user_id, flight_id, trip_type, departure_date, return_date, luggage_type, seat_count, passenger_names)
        trip_id = self.trip_repository.save(trip)
        return {"trip_id": trip_id, "total_cost": total_cost}
