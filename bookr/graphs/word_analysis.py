from bookr.tasks import word_analysis
from bookr.taskmanage import taskgraph


def create_taskgraph():
    graph = taskgraph.Taskgraph()

    for task in word_analysis.create_tasks():
        graph.append_task(task)

    return graph