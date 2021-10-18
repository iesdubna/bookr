import requests

link = 'https://www.gutenberg.org/cache/epub/2302/pg2302-images.html'
file = "Poor_Folk.txt"

with requests.get(link, stream=True) as response:
    with open(file, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)