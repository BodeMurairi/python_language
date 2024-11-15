from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/news"  # Corrected URL

response = requests.get(url)
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")

articles = soup.find_all("a", class_="storylink")  # Filter by class
article_names = []
article_links = []
article_upvotes = []

for article in articles:
    print(article)

upvotes = soup.find_all("span", class_="score")  # Find upvote elements separately

for upvote in upvotes:
    # Extract integer upvote value (assuming score is within the span)
    upvote_value = int(upvote.text.strip().split()[0])  # Split and pick first word
    article_upvotes.append(upvote_value)

print(article_names)
print(article_links)
print(article_upvotes)

