import requests
from datetime import datetime

USERNAME = "bode"
TOKEN = "6Y9QOZLTNM"
GRAPH_ID = "graph1"

user_params = {
    "token": "6Y9QOZLTNM",
    "username": "bode",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}


pixela_endpoint = "https://pixe.la/v1/users"

#response = requests.post(url = pixela_endpoint, json= user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graphic_config = {
    "id": GRAPH_ID,
    "name": "My coding graph",
    "unit": "min",
    "type": "int",
    "color": "momiji"
}
headers ={
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url= graph_endpoint, json=graphic_config, headers= headers)
#print(response.text)

graph_postValue_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"
today_date = datetime.now()
#print(today_date.strftime("%Y%m%d"))
value_config = {
    "date": today_date.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you work today?:"),
    "string": "Day36 challenge completed"
}

value_header = {
    "X-USER-TOKEN": TOKEN
}
response = requests.post(url=graph_postValue_endpoint, json=value_config, headers=value_header)
print(response.text)

update_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/20241019"

update_params = {
    "quantity": "240"
}

update_header = {
"X-USER-TOKEN": TOKEN
}

#response = requests.put(url= update_endpoint, json= update_params, headers=update_header)
#print(response.text)

delete_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/20241020"

delete_header = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.delete(url=delete_endpoint, headers=delete_header)
#print(response.text)