class Trip:
    def __init__(self, trip_cities, start_date):
        self.trip_cities = trip_cities
        self.start_date = start_date
        self.aircraft = None
        self.trip_route = None
        self.cost = None
    
    def __repr__(self):
        return f'Trip: {self.trip_cities} Aircraft: {self.aircraft} rout: {self.trip_route} cost: {self.cost}'