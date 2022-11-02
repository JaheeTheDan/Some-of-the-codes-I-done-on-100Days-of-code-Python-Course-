from requests import get

class DataManager:
    '''Read data from google sheet'''

    def __init__(self):
        self.api_endpint='https://api.sheety.co/b45b65668e3451c564c4f538cf9008e8/copyOfFlightDeals/prices'

        self.__header={
            "Authorization": ''
        }
    def flight_to_check(self):
        '''return dictionary with citys wanted to go and there lowest price'''
        response=get(self.api_endpint,headers=self.__header, timeout=10)
        response.raise_for_status()
        return response.json()['prices']
