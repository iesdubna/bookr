import yaml

from pprint import pprint
import requests

with open("books.yaml" , "r") as c:
    data = yaml.safe_load(c)

pprint(data)

for item in data["books"]:
    path = "books/" + item["filename"]




    with requests.get(item["link"], stream=True) as response:
        with open(path, "wb")  as c:
            for chunk in response.iter_content(chunk_size=8192):
                 c.write(chunk)
