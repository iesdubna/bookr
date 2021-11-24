from bookr.taskmanage import taskgraph
from bookr.tasks import download
from bookr.tasks import word_analysis
from bookr.tasks import sentence_analysis

def create_taskgraph():
    graph = taskgraph.Taskgraph()
    download_tasks = download.create_tasks()
    word_analysis_tasks = word_analysis.create_tasks()
    sentence_analysis_tasks = sentence_analysis.create_tasks()
    
    for i in range(0,len(download_tasks)):
        task0=download_tasks[i]
        task1=word_analysis_tasks[i]
        task2=sentence_analysis_tasks[i]
        task1.depends_on(task0)
        task2.depends_on(task0)

        graph.append_task(task1)
        graph.append_task(task2)
        graph.append_task(task0)
    return graph