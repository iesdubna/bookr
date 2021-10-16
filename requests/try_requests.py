import requests

link = "https://www.gutenberg.org/files/174/174-0.txt"
file = "picture_of_dorian_grey.txt"

with requests.get(link, stream=True) as response:
    with open(file, "wb")as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
