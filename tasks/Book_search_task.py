import requests

link = 'https://www.gutenberg.org/cache/epub/61/pg61.txt'
file = "Karl_Marx.txt"

with requests.get(link, stream=True) as response:
    with open(file, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)