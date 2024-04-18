from pymongo import MongoClient
from flight.domain.entities.flight import Flight

class MongoDBFlightRepository:
    def __init__(self, connection_string, database_name):
        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]
        self.collection = self.db['flights']

    def save(self, flight: Flight):
        flight_data = {
            'city': flight.city,
            'state': flight.state,
            'date': flight.date,
            'price': flight.price
        }
        result = self.collection.insert_one(flight_data)
        flight.id = str(result.inserted_id)

    def find_by_city_and_date(self, city, date):
        query = {'city': city, 'date': date}
        results = self.collection.find(query)
        return [Flight(r['city'], r['state'], r['date'], r['price'], str(r['_id'])) for r in results]
    
    def find_all(self):
        flights_data = self.collection.find()
        return [Flight(f['city'], f['state'], f['date'], f['price'], str(f['_id'])) for f in flights_data]
    
    def find_by_city_or_state(self, city=None, state=None):
        query = {}
        if city:
            query['city'] = city
        if state:
            query['state'] = state
        flights_data = self.collection.find(query)
        return [Flight(f['city'], f['state'], f['date'], f['price'], str(f['_id'])) for f in flights_data]
    
    def find_by_city(self, city):
        flights_data = self.collection.find({"city": city})
        return [Flight(f['city'], f['state'], f['date'], f['price'], str(f['_id'])) for f in flights_data]

    def find_by_state(self, state):
        flights_data = self.collection.find({"state": state})
        return [Flight(f['city'], f['state'], f['date'], f['price'], str(f['_id'])) for f in flights_data]