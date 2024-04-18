from datetime import datetime

def validate_dates(departure_date, return_date=None):
    try:
        departure = datetime.strptime(departure_date, '%Y-%m-%d')
        if return_date:
            return_ = datetime.strptime(return_date, '%Y-%m-%d')
            return departure < return_
        return True
    except ValueError:
        return False

def validate_luggage(luggage_type):
    return luggage_type in ['basic', 'medium', 'premium']
