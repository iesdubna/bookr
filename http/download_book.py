import requests

link = "https://www.gutenberg.org/cache/epub/44171/pg44171.txt"
file = "America's_Postal_System.txt"

with requests.get(link, stream=True) as response:
    with open(file, "wb")as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)