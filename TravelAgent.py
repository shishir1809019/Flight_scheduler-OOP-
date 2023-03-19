from AllAirports import AllAirports
from AirLines import AirLines

class TravelAgent:
    def __init__(self, name):
        self.name = name
        self.trips = None
        self.all_airports = AllAirports()
        self.air_lines = AirLines()
    
    def set_trip_one_city_one_way(self, start, end, start_date):
        self.all_airports.get_ticket_price(start, end)

    def set_trip_one_city_two_way(self):
        pass
    
    def set_trip_multi_city_one_way(self):
        pass

    def set_trip_multi_city_round(self):
        pass

    



