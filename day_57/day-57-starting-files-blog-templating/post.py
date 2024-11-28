import requests
class Post:
    """ class rendering all the posts on the website"""
    def __init__(self):
        self.api_endpoint = "https://api.npoint.io/c790b4d5cab58020d391"
        self.posts = requests.get(url= self.api_endpoint).json()




