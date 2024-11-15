from bs4 import BeautifulSoup
import requests
import pandas as pd

web_link = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(web_link)
soup = BeautifulSoup(response.text, "html.parser")
soup.prettify() # Format HTML

movies = soup.find_all("h3")
best_movies = []
for movie in movies:
    best_movies.append(movie.string) # fetch movies title

best_movies = list(reversed(best_movies)) # reversed list
#print(best_movies)

cleaned_list = [movie[movie.find(')')+2:] if ')' in movie else movie for movie in best_movies] # Clean movies list

my_movies = pd.DataFrame(cleaned_list, columns=["Best Movies"])
my_movies.to_csv("./movies.csv", index=False)
print(my_movies)