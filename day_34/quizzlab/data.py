import requests
import json

api_url = "https://opentdb.com/api.php?amount=10&type=boolean"
api_parameters = {
    "amount": 10,
    "type": "boolean"
}

data = requests.get(api_url, params=api_parameters)
data.raise_for_status()
data = data.json()
question_data = data["results"]
