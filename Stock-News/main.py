from requests import get
from twilio.rest import Client

#API keys goes below
ACCOUNT_SID= ''
AUTH_TOKEN = ''
STOCK_API_KEY= ''
NEWS_API_KEY = ''

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

client = Client(ACCOUNT_SID,AUTH_TOKEN )

def differences():
    '''Calculate the differences between yesturday closing price and day before closing price,
    return a negative or positive percentage difference'''

    def get_stock_data()->dict:
        response= get(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={STOCK_API_KEY}')
        response.raise_for_status()
        return response.json()

    data = get_stock_data()
    last_rfresh_date = data['Meta Data']['3. Last Refreshed']
    day=last_rfresh_date[8:]
    prev_date = last_rfresh_date[:8]+str(int(day)-1)

 
    last_rfresh_date_close_data = float(data['Time Series (Daily)'][last_rfresh_date]['4. close'])
    prev_date_close_data = float(data['Time Series (Daily)'][prev_date]['4. close'])

    difference = last_rfresh_date_close_data-prev_date_close_data
    difference_percent = round(difference/last_rfresh_date_close_data*100)

    return difference_percent


def get_news_pieces()->list:
    '''Get news articles based on the company name'''
    news_pieces = []

    params={
        'q': COMPANY_NAME,
        'searchIn':'title',
        'apiKey': NEWS_API_KEY,
        'pageSize': 3
        }
    response = get('https://newsapi.org/v2/everything?', params=params)
    response.raise_for_status()

    # format the news articles
    for news in response.json()['articles']:
        text=f"From {news['source']['name']}\n{news['title']}\nBrief: {news['description']}\nLink: {news['url']}"
        news_pieces.append(text)

    return news_pieces


def send_sms(text='test', goes_up=''):
    '''Send a SMS message to inputed phone number'''
    if goes_up:
        text = ''
    message = client.messages.create(
        body = text,
        from_ = '+18454091059',
        to = '' # user phone goes here
    )
    print(message.sid)



differences_percent = differences()
if differences_percent > 5:
    send_sms(f'{STOCK} stock increase by {differences_percent}%')
    for news in get_news_pieces():
        send_sms(news)
elif differences_percent < -5:
    send_sms(f'{STOCK} stock decrease by {str(differences_percent)[1:]}%')
    for news in get_news_pieces():
        send_sms(news)
