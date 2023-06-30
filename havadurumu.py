import requests

url = "http://api.weatherapi.com/v1/current.json"
access_key = "e93eab8d34354830869130508230306"

response = requests.get(url,params = {
    "key": access_key,
    "q": "Gaziantep",
    "lang":"tr"
})

resp = response.json()

print(resp)