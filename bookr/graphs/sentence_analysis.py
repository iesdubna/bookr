from bookr.tasks import sentence_analysis
from bookr.taskmanage import taskgraph


def create_taskgraph():
    graph = taskgraph.Taskgraph()

    for task in sentence_analysis.create_tasks():
        graph.append_task(task)

    return graph