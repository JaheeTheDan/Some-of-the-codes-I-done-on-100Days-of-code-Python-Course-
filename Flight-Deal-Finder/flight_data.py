class FlightData:
    '''A class that formats flight data'''

    def __init__(self, data):
        self.data = data

        self.flight_data = {
            'from_flight':'',
            'to_flight':'',
            'price':'',
            'local_arrival_date':'',
            'local_departure_date':'',
            'link':''
        }

    def sort_flight_data(self):
        '''Sort the data'''
        for i in self.data:
            self.flight_data['from_flight'] = f"{i['flyFrom']}, {i['cityFrom']}, {i['countryFrom']['name']},"
            self.flight_data['to_flight'] = f"{i['flyTo']}, {i['cityTo']}, {i['countryTo']['name']},"
            self.flight_data['price'] = i['price']
            self.flight_data['local_arrival_date'] = i['local_arrival'][0:10]
            self.flight_data['local_departure_date'] = i['local_departure'][0:10]
            self.flight_data['link'] = i['deep_link']

        return self.flight_data
