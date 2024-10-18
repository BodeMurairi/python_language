import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -1.970579 # Your latitude
MY_LONG = 30.104429 # Your longitude
My_email = "bodemurairi2@gmail.com"
My_password = "jhgxuxvcfgemsewq"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    #Your position is within +5 or -5 degrees of the ISS position.
    parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    #If the ISS is close to my current position
    if MY_LAT - 5 <=iss_latitude>= MY_LAT+5  and MY_LONG-5 <= iss_longitude >= MY_LONG+5:
        return True
    

# and it is currently dark
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >= sunrise or time_now >= sunset:
        return True
# Then send me an email to tell me to look up.
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(My_email, My_password)
            connection.sendmail(from_addr=My_email,
                            to_addrs= My_email,
                            msg=f"Subject: LOOK UP\n\n The ISS is above you in the sky")


