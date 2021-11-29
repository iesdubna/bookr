from bookr.taskmanage import taskgraph
from bookr.tasks import download
from bookr.tasks import word_analysis
from bookr.tasks import sentence_analysis
from bookr.tasks import dendrogram

def create_taskgraph():
    graph = taskgraph.Taskgraph()
    download_tasks = download.create_tasks()
    word_analysis_tasks = word_analysis.create_tasks()
    sentence_analysis_tasks = sentence_analysis.create_tasks()
    dendrogram_task = dendrogram.create_task()
    graph.append_task(dendrogram_task)

    for i in range(0, len(download_tasks)):
        word_analysis_tasks[i].depends_on(download_tasks[i])
        sentence_analysis_tasks[i].depends_on(download_tasks[i])
        dendrogram_task.depends_on(word_analysis_tasks[i])

        graph.append_task(download_tasks[i])
        graph.append_task(word_analysis_tasks[i])
        graph.append_task(sentence_analysis_tasks[i])
    return graph
