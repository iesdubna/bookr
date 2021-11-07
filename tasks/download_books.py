import yaml
import requests 
from taskmanage.task import Task 
from functools import partial


def download(bookpath, link):
    with requests.get(link, stream=True) as response:
        with open(bookpath, "wb")  as c:
            for chunk in response.iter_content(chunk_size=8192):
                 c.write(chunk)
                

def create_tasks():
    with open("books.yaml") as f:
        config = yaml.safe_load(f) 

    tasks=[]
    for book in config["books"]:
        path = "books/" + book["filename"]
        task = Task(path)
        funk_without_arguments = partial(download, path , book["link"])
        task.set_action(funk_without_arguments)

        tasks.append(task)
    return tasks 
