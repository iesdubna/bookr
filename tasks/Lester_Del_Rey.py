import time
import requests
from taskmanage import task

def download_book_0():
    link = 'https://www.gutenberg.org/cache/epub/51168/pg51168.txt'
    file = "Operation_distress.txt"

    with requests.get(link, stream=True) as response:
        with open(file, "bw") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)


task0 = task.Task("0")
task0.set_action(download_book_0)

taskgraph = task.Taskgraph()
taskgraph.append_task(task0)

#taskgraph.run_correct_order()
taskgraph.run_in_threads()