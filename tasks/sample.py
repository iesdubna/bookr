from taskmanage import task

def fake_download_file_1():
    print("Download file 1 ...")

def fake_download_file_2():
    print("Download file 2 ...")

def fake_augment_file_1():
    print("Augment file 1 ...")

def fake_do_analysis_1_file_1_2():
    print("Do analysis 1 of files 1 and 2 ...")

def fake_do_analysis_2_file_1():
    print("Do analysis 2 of file 1 ...")

task0 = task.Task("0")
task0.set_action(fake_download_file_1)

task1 = task.Task("1")
task1.set_action(fake_download_file_2)

task2 = task.Task("2")
task2.set_action(fake_augment_file_1)

task3 = task.Task("3")
task3.set_action(fake_do_analysis_1_file_1_2)

task4 = task.Task("4")
task4.set_action(fake_do_analysis_2_file_1)

task2.depends_on(task0)
task3.depends_on(task1)
task3.depends_on(task2)
task4.depends_on(task2)

taskgraph = task.Taskgraph()
taskgraph.append_task(task0)
taskgraph.append_task(task1)
taskgraph.append_task(task2)
taskgraph.append_task(task3)
taskgraph.append_task(task4)

taskgraph.run()
