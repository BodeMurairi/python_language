import requests

def get_article_data():
    api_endpoint = "https://api.npoint.io/a5992a4597cf09131377"
    response = requests.get(api_endpoint).json()
    for article in response:
        article_title = article["title"]
        article_subtitles = article["subtitle"]
        article_body = article["body"]
        article_image_url = article["image_url"]


get_article_data()