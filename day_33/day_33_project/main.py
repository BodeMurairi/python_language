import requests
import json
from datetime import datetime

my_lat = -1.970579
my_long = 30.104429
parameters = {
    "lat": my_lat,
    "lng": my_long,
    "formatted": 0
}



response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
current_time = datetime.now()
print(current_time.hour)