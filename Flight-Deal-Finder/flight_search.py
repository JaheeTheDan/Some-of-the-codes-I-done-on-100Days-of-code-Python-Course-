from requests import get
from datetime import datetime
from dateutil.relativedelta import relativedelta

class FlightSearch:
    '''Use the tequila api to search for the cheapest flights'''
    def __init__(self,from_flight,to_flight):
        self.__header = {
            'apikey':''
        }

        self.today_date = datetime.strftime(datetime.now(),'%d/%m/%Y')
        self.next_six_month_date = datetime.strftime(datetime.now()+ relativedelta(months=6),'%d/%m/%Y')

        self.param={
            'fly_from': from_flight,
            'fly_to' : to_flight,
            'date_from': self.today_date,
            'date_to': self.next_six_month_date,
            'curr':'GBP',
            'sort':'price',
            'asc':1,
            'limit': 1
        }

        self.api_endpoint='https://api.tequila.kiwi.com/v2/search'

    def find_flight(self):
        '''Look for flight and return a dictionary'''
        response = get(self.api_endpoint,params=self.param, headers=self.__header, timeout=10)
        response.raise_for_status()
        return response.json()['data']
