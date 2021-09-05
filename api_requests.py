import requests

response = requests.get("https://api.spotify.com/v1/albums")
print(response.status_code)