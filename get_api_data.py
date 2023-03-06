import requests
import json

url = 'https://restcountries.com/v3.1/name/Poland'
response = requests.get(url)
print(response.json())