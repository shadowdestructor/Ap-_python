from urllib import response
import requests
headline = "https://newsapi.org/v2/top-headlines"
'''response = requests.get("https://newsapi.org/v2/everything",params=
        {
            'apiKey': 'd6936ea1221c4f7992a4342b74f18d4b',
            'q': 'ekonomi',
            'language': 'tr',
            'sortBy': 'publishedAt',
            'pageSize': '10'
        })
'''
response = requests.get(headline, params={
     "apiKey": 'd6936ea1221c4f7992a4342b74f18d4b',
     "country": "tr"
 })
resp = response.json()["articles"]

for i in resp:
    print(i["source"]["name"])
    print(i["title"])
    #print(i["description"])
    print(i["url"])
    #print(i["publishedAt"])
    #print(i["urlToImage"])