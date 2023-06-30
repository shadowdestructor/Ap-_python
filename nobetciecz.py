import requests

api_key = "apikey 1LEtzE93yKFHMaGzuuIzib:7gpvIy4MgtjKtOtvxgM1ZU"

url = "https://api.collectapi.com/health/dutyPharmacy?ilce=şahinbey&il=Gaziantep"

response = requests.get(url,headers={
    'authorization': api_key,
    'content-type': "application/json",
})

resp = response.json()

print(resp)