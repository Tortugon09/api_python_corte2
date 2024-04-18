class Trip:
    def __init__(self, user_id, flight_id, trip_type, departure_date, return_date, luggage_type, seat_count, passenger_names, trip_id=None):
        self.user_id = user_id
        self.flight_id = flight_id
        self.trip_type = trip_type
        self.departure_date = departure_date
        self.return_date = return_date
        self.luggage_type = luggage_type
        self.seat_count = seat_count
        self.passenger_names = passenger_names
        self.trip_id = trip_id  # Manejar el _id de MongoDB si es necesario

    def serialize(self):
        return {
            "user_id": self.user_id,
            "flight_id": self.flight_id,
            "trip_type": self.trip_type,
            "departure_date": self.departure_date,
            "return_date": self.return_date if self.return_date else None,  # Manejar fechas de retorno opcionales
            "luggage_type": self.luggage_type,
            "seat_count": self.seat_count,
            "passenger_names": self.passenger_names,
            "trip_id": self.trip_id
        }
