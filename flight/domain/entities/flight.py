class Flight:
    def __init__(self, city, state, date, price, flight_id=None):
        self.city = city
        self.state = state
        self.date = date
        self.price = price
        self.id = flight_id
