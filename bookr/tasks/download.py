from functools import partial

import requests

from bookr import cfg
from bookr.taskmanage import task


def download(path, link):
    with requests.get(link, stream=True) as response:
        with open(path, "wb")  as c:
            for chunk in response.iter_content(chunk_size=8192):
                 c.write(chunk)
                

def create_tasks():
    tasks=[]
    for book in cfg.CONF["books"]:
        path = cfg.datapath(book["txt_file"])
        t = task.Task(book["link"])
        funk_without_arguments = partial(download, path , book["link"])
        t.set_action(funk_without_arguments)
        tasks.append(t)
    return tasks 
