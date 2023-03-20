from TravelAgent import TravelAgent

def main():
    travel_agent = TravelAgent('Sullah_Airlines')
    trip_info1 = travel_agent.set_trip_one_city_one_way('DAC', 'PRA', '31/12/2066')
    # print('aircraft: ', trip_info1.aircraft)
    # print('price: ', trip_info1.price)

    trip_cities = ['DUB', 'LHR', 'SYD', 'JFK']
    trip_info2 = travel_agent.set_trip_multi_city_flexible_route(trip_cities, '11/12/2065')
    print('price: ', trip_info2[1])
    for trip in trip_info2[0]:
        print(trip)

if __name__ == '__main__':
    main()