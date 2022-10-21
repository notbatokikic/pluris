import json
import requests
from jinja2 import Environment, FileSystemLoader

request = requests.get("https://ftx.com/api/markets/XRP/USD")
request2 = requests.get("https://api.thecatapi.com/v1/images/search?breed_ids=beng")
request2 = request2.json()



def call():
    response = request.json()["result"]
    return response

def calling():
    print(json.dumps(request2, sort_keys=True, indent=4))
    return request2

calling()



