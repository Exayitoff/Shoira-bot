import requests
r = requests.get('https://api.thecatapi.com/v1/images/search?limit=1')

data = r.json()[0]
print(data)