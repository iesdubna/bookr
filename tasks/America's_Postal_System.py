import time
import requests
from taskmanage import task

def download_book_1():
    link = "https://www.gutenberg.org/cache/epub/44171/pg44171.txt"
    file = "America's_Postal_System.txt"

    with requests.get(link, stream=True) as response:
        with open(file, "wb")as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

task1 = task.Task("1")
task1.set_action(download_book_1)

taskgraph = task.Taskgraph()
taskgraph.append_task(task1)

taskgraph.run_in_threads()

