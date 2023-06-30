import requests

class Film():
    def __init__(self):
        self.url = 'https://api.themoviedb.org/3'
        self.api_key = '7fd77424f76a6b78979c201e3a4907f3'
    def populate(self):
        response = requests.get(f"{self.url}/movie/popular?api_key={self.api_key}&language=&page=1")
        return response.json()
    def keyword(self,key):
        response = requests.get(f"{self.url}/search/movie?api_key={self.api_key}&language=en-US&query={key}&page=1")
        return response.json()

filmler = Film()

print(filmler.populate())