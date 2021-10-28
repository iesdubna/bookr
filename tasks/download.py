import yaml
from taskmanage.task import Task
import requests
from functools import partial

with open("books.yaml") as c:
    data = yaml.safe_load(c)


def download(bookpath):
    for item in data["books"]:
        path = "books/" + item["filename"]
        with requests.get(item["link"], stream=True) as response:
            with open(path, "wb")  as c:
                for chunk in response.iter_content(chunk_size=8192):
                    c.write(chunk)


def create_tasks():


    tasks = []

    for item in data["books"]:
        path = "books/" + item["filename"]
        task = Task(path)
        funk_without_arguments = partial(download, path)
        task.set_action(funk_without_arguments)

        tasks.append(task)

    return tasks

for t in create_tasks():
    t.run()

