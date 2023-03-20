import csv
from Aircraft import Aircraft

class AirLines:
    def __init__(self):
        self.air_crafts = None
        self.load_air_crafts_data('Module/M-20/data/aircraft.csv')

    def load_air_crafts_data(self, csv_file_path):
        air_crafts = {}
        with open(csv_file_path, 'r') as file:
            lines = csv.reader(file)
            next(lines)
            
            for line in lines:
                air_crafts[line[0]] = Aircraft(line[3], line[0], line[1], line[4])
        file.close()
        self.air_crafts = air_crafts

    def get_air_crafts(self, aircraft_code):
        return self.air_crafts[aircraft_code]
    
    def get_aircraft_by_distance(self, distance):
        for aircraft in self.air_crafts.values():
            if aircraft.flight_range < distance:
                return aircraft
