import time
from taskmanage import task
import requests

link = 'https://www.gutenberg.org/files/65770/65770-0.txt'
file = "the_killer.txt"

def book_downl():
    with requests.get(link, stream=True) as response:
        with open(file, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)


task1 = task.Task("1")
task1.set_action(book_downl)

taskgraph = task.Taskgraph()
taskgraph.append_task(task1)

#taskgraph.run_correct_order()
taskgraph.run_in_threads()