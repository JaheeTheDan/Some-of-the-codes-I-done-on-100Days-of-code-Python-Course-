import datetime
import requests

#Info for TrackApi
TRACKAPI_URL='https://trackapi.nutritionix.com/v2/natural/exercise'
TRACKAPI_APP_ID=''
TRACKAPI_API_KEY=''

#Info for SheetyApi
SHEETY_URL = 'https://api.sheety.co/b45b65668e3451c564c4f538cf9008e8/copyOfMyWorkouts/workouts'
SHEETY_API_KEY=''

#Info based on user 
GENDER= 'male'
WEIGHT=75
HEIGHT=150
AGE=20


def get_data_from_trackapi()->list:
    '''Ask the user for kind of exercises was performed and return a list of data based what was input'''
    workout_info = input('What exercise you did? ')

    headers = {
        "x-app-id": TRACKAPI_APP_ID,
        'x-app-key': TRACKAPI_API_KEY
    }
    params = {
        'query': workout_info,
        'gender': GENDER,
        'weight_kg':WEIGHT,
        'height_cm': HEIGHT,
        'age':AGE

    }

    response = requests.post(TRACKAPI_URL,json=params,headers=headers)
    response.raise_for_status()
    data = response.json()


    return data['exercises']


def put_data_in_google_sheet(data):
    '''Format the data and put it in a google sheet'''

    headers={
        "Authorization": SHEETY_API_KEY
    }
    sheet_data={
        'workout':{
            'date': datetime.datetime.now().strftime('%d/%m/%Y'),
            'time':datetime.datetime.now().strftime('%I:%M %p'),
            'exercise': data['name'].title(),
            'duration': f"{data['duration_min']} minutes",
            'calories' : data['nf_calories']
        }
    }
    response = requests.post(SHEETY_URL,json=sheet_data, headers=headers)
    response.raise_for_status()
    print(response.text)


for i in get_data_from_trackapi():
    put_data_in_google_sheet(i)
