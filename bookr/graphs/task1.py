from __init__ import GRAPH_FACTORY
from bookr.taskmanage import taskgraph
from bookr.taskmanage import task
import threading

def taskgraph1():
    tasks=[]
    tasks_download=GRAPH_FACTORY('download')()
    tasks_word_analysis=GRAPH_FACTORY('word_analysis')()
    tasks_sentence_analysis=GRAPH_FACTORY('sentence_analysis')()

    task0 = task.Task("0")
    task1 = task.Task("1")
    task2 = task.Task("2")
    for i in range(0,len(tasks_download)):
        task0=tasks_download[i]
        task1=tasks_word_analysis[i]
        task2=tasks_sentence_analysis[i]
        task1.depends_on(task0)
        task2.depends_on(task0)

    taskgraph = taskgraph.Taskgraph()
    taskgraph.append_task(task1)
    taskgraph.append_task(task2)
    taskgraph.append_task(task0)
    tasks.append(taskgraph)

    taskgraph.run_in_threads()