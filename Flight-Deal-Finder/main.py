from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager

FROM_CITY='LHR'
places_wanted_to_go = DataManager().flight_to_check()
for i in places_wanted_to_go:
    city=i['iataCode']
    data = FlightData(FlightSearch(FROM_CITY,city).find_flight()).sort_flight_data()

    if int(i['lowestPrice']) >= data['price']:
        NotificationManager(data).send_notification()
