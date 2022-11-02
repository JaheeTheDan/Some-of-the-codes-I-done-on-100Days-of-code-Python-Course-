from twilio.rest import Client

class NotificationManager:
    '''Send a notification to user when a flight that is cheap'''

    def __init__(self,info):
        self.__account_sid = ''
        self.__auth_token = ''
        self.client = Client(self.__account_sid, self.__auth_token)
        self.body = f"Low price alert! Only £{info['price']} to fly from {info['from_flight']} to {info['to_flight']}"\
            f"From {info['local_arrival_date']} to {info['local_departure_date']} "\
            f"\n{info['link']}"

    def send_notification(self):
        '''Used the twillo API to send notification to user'''
        message = self.client.messages.create(
                    body=self.body,
                    from_='+18454091059',
                    to='+18765373710'
                )
        print(message.sid)
