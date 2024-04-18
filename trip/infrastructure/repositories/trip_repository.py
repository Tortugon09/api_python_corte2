from pymongo import MongoClient
from bson.objectid import ObjectId
from trip.domain.entities.trip import Trip

class TripRepository:
    def __init__(self, connection_string, database_name):
        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]
        self.collection = self.db['trips']

    def save(self, trip: Trip):
        trip_data = vars(trip)
        result = self.collection.insert_one(trip_data)
        return str(result.inserted_id)
    
    def find_by_user_id(self, user_id):
        trips_data = self.collection.find({"user_id": user_id})
        trips = []
        for data in trips_data:
            # Asegúrate de extraer solo los campos necesarios
            trip = Trip(
                user_id=data['user_id'],
                flight_id=data['flight_id'],
                trip_type=data['trip_type'],
                departure_date=data['departure_date'],
                return_date=data.get('return_date'),  # Usa get para campos opcionales
                luggage_type=data['luggage_type'],
                seat_count=data['seat_count'],
                passenger_names=data['passenger_names']
            )
            trips.append(trip)
        return trips

    def get_flight_price(self, flight_id):
        try:
            # Asegúrate de que el ID esté en el formato adecuado
            object_id = ObjectId(flight_id)
            flight_data = self.db['flights'].find_one({"_id": object_id}, {'price': 1})
            if flight_data and 'price' in flight_data:
                return flight_data['price']
            else:
                raise ValueError(f"No valid flight found for ID {flight_id} or price is missing.")
        except Exception as e:
            raise Exception(f"Failed to retrieve flight price: {str(e)}")