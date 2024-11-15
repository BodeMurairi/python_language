from bs4 import BeautifulSoup


with open("C:/Users/nn/Documents/python_language/day_45/bs4-start/bs4-start/website.html") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
anchor_tags = soup.find_all(name="a")
for tag in anchor_tags:
    print(tag.getText())

for tag in anchor_tags:
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
company_url = soup.select_one(selector="p a")
print(company_url)
