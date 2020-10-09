import requests

BASE = "http://127.0.0.1:5000/pokemon/"


response = requests.get(BASE + "all")
print(response.json())

reponse = requests.get(BASE + "1")
print(response.json())

response = requests.get(BASE + "ditto")
print(response.json())
