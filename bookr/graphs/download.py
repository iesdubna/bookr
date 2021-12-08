from bookr.tasks import download
from bookr.taskmanage import taskgraph


def create_taskgraph():
    graph = taskgraph.Taskgraph()

    for task in download.create_tasks():
        graph.append_task(task)

    return graph