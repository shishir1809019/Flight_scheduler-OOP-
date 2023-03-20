class Trip:
    def __init__(self, trip_cities, aircraft, price, start_date, route = ''):
        self.trip_cities = trip_cities
        self.aircraft = aircraft
        self.price = price
        self.start_date = start_date
        self.trip_route = route
    
    def __repr__(self):
        return f'Trip: {self.trip_cities} cost: {self.price}'