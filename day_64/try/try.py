import requests

TMBD_API_KEY = "27d315fba447cf43a44757411b45e3ca"
SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

movie_title = "avatar"

response = requests.get(url=SEARCH_URL, params={"api_key": TMBD_API_KEY, "query": movie_title})
response.raise_for_status()
film_data = response.json()
print(film_data)

movie_id = film_data["results"][0]["id"]
#print(movie_id)


movie_api_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
response = requests.get(url=movie_api_url, params={"api_key": TMBD_API_KEY, "language": "en-US"})
response.raise_for_status()
movie_data = response.json()
print(movie_data)