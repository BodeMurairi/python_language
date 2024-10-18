import requests
import json
from twilio.rest import Client
import os

api_url = "http://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OMW_API_KEY")
latitude = -1.970579
longitude = 30.104429

account_sid = "ACc048d9b1b9ab16e31f16edd5aff2ec23"
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key,
    "cnt": 4
}

data = requests.get(api_url, params=parameters)
data.raise_for_status()
weather_data = data.json()

segment_weather = weather_data["list"]
#id_weather = segment_weather[0]["weather"][0]["id"]

#if id_weather < 700 :
#    print("It is going to run. Don't forget to bring your umbrella")
will_rain = False
for hour_data in segment_weather:
   condition_code = hour_data["weather"][0]["id"]
   if int(condition_code) < 700:
       will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It is going to rain today. Remember to bring your ☂",
        from_="+18644002574",  # Remove space after comma
        to="+250795020998"
    )
    print(message.status)