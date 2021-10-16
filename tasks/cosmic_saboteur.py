import time
from taskmanage import task
import requests

link = 'https://www.gutenberg.org/cache/epub/66540/pg66540.txt'
file = "cosmic_saboteur.txt"

def download():
    with requests.get(link, stream=True) as response:
        with open(file, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)


task0 = task.Task("0")
task0.set_action(download)



taskgraph = task.Taskgraph()
taskgraph.append_task(task0)

#taskgraph.run_correct_order()
taskgraph.run_in_threads()
