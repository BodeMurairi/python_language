import requests

try:
    response = requests.get(url="http://open-notify.org/Open-Notify-API/ISS-Location-Now/")
    data = response.json()
    print(data)
except JSONDecodeError:
    print("Error: Invalid JSON data received from API.")