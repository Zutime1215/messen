import json
import requests

with open("configme.txt") as file:
    data = json.loads(file.read())
    url = data["url"]
    r = requests.get(url).text
    print(r)
