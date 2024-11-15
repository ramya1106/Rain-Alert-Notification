import requests
from twilio.rest import Client
import os

api_key = os.environ.get('API_KEY')
api_url = "https://api.openweathermap.org/data/2.5/weather"

parameters = {
    "lat": 14.4333,
    "lon": 79.9667,
    "appid": api_key,
    "exclude": "currently,minutely,daily"
}
response = requests.get(url=api_url, params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False

weather_slice = data["rain"]["1h"]
if weather_slice > 1:
    will_rain = True

if will_rain:
    account_sid = 'AC806ab79171bb9eaa37ba303d9b085f21'
    auth_token = 'e10639ae88724e7d43a5ed20447611a7'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today.\nRemember to bring an umbrella ☔.",
        from_=os.environ.get('FROM_NUM'),
        to=os.environ.get('TO_NUM')
    )

    print(message.status)
