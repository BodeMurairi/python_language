import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

billboard_url = "https://www.billboard.com/charts/hot-100/"

response = requests.get(billboard_url)

website = response.text

soup = BeautifulSoup(website, "html.parser")
songs = soup.select("li ul li h3")
best_songs = [song.getText().strip() for song in songs]

spotify_client_ID = "30547730d7d14983aa4cc048732f307c"
spotify_client_secret = "bd33f4aeda9b4694ab3a54d7a5f596db"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri ="http://example.com",
        client_id = spotify_client_ID,
        client_secret = spotify_client_secret,
        show_dialog=True,
        cache_path="token.txt",
        username = "Billboard playlist", 
    )
)
user_id = sp.current_user()["id"]
#print(user_id)
spotify_client_token = "312y2wuxm5xuli7maytsm26iwtne"

year = 2024
song_uris = []
for songs in best_songs:
    result = sp.search(q=f"track: {songs} year: {year}", type="track")
    print(result)
    try:
        uri= result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{songs} doesn't exist in Spotify. Skipped.")


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=spotify_client_ID,
        client_secret= spotify_client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
song_uris = ["The list of", "song URIs", "you got by", "searching Spotify"]

playlist = sp.user_playlist_create(user= user_id, name=f"{year} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)