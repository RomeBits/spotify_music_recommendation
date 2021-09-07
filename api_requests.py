import requests

# Authorize our application
url = "https://accounts.spotify.com/authorize"
headers = {
    "client_id": "ae94085f9ba742fc811ec3ecfbc1e864",
    "response_type": "code",
    "redirect_uri": "http://127.0.0.1:5500/spotify_music_recommendation/index.html"
}

response = requests.get(url, headers)
print(response)