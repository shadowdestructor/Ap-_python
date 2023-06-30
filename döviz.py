import requests

url = "https://api.collectapi.com/economy/currencyToAll?int=10&base=USD"
api_key = "apikey 1LEtzE93yKFHMaGzuuIzib:7gpvIy4MgtjKtOtvxgM1ZU"

response = requests.get(url,headers = {
    'authorization':api_key,
    'content-type': "application/json"
    })

resp = response.json()


print(resp)