import requests
import json

class AgeGender:
    def __init__(self):
        self.agify_url_endpoint = "https://api.agify.io"
        self.genderize_url_endpoint = "https://api.genderize.io"
        self.person_name = input("Enter your name:")
        self.params = {"name": self.person_name}
        self.age_data = None
        self.age = None
        self.gender_data = None
        self.gender = None
        self.probability = None


    def agerize(self):
        self.age_data = requests.get(self.agify_url_endpoint, params=self.params).json()
        self.age = self.age_data['age']
        return self.age

    def genderize(self):
        self.genderize_data = requests.get(self.genderize_url_endpoint, params=self.params).json()
        self.gender = self.genderize_data['gender']
        self.probability = self.genderize_data['probability']
        return self.gender, self.probability
