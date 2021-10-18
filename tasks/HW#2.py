from taskmanage import task
import requests

def searсh_book():
    link = 'https://www.gutenberg.org/cache/epub/61/pg61.txt'
    file = "Karl_Marx.txt"

    with requests.get(link, stream=True) as response:
        with open(file, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print("Book_already_booted")

task1=task.Task("1")
task1.set_action(searсh_book)

taskgraph = task.Taskgraph()
taskgraph.append_task(task1)

taskgraph.run_in_threads()