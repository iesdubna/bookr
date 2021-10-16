import requests
from taskmanage import task
import time

link = 'https://www.gutenberg.org/files/2554/2554-0.txt'
file = "Crime_and_Punishment.txt"

def book():
    with requests.get(link, stream=True) as response:
        with open(file, "wb") as c:
            for chunk in response.iter_content(chunk_size=8192):
                c.write(chunk)

