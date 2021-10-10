import time
from taskmanage import task

def fake_action_0():
    print("Start action 0")
    time.sleep(1)
    print("Stop action 0")

def fake_action_1():
    print("Start action 1")
    time.sleep(10)
    print("Stop action 1")

def fake_action_2():
    print("Start action 2")
    time.sleep(1)
    print("Stop action 2")

def fake_action_3():
    print("Start action 3")
    time.sleep(3)
    print("Stop action 3")

def fake_action_4():
    print("Start action 4")
    time.sleep(1)
    print("Stop action 4")

task0 = task.Task("0")
task0.set_action(fake_action_0)

task1 = task.Task("1")
task1.set_action(fake_action_1)

task2 = task.Task("2")
task2.set_action(fake_action_2)

task3 = task.Task("3")
task3.set_action(fake_action_3)

task4 = task.Task("4")
task4.set_action(fake_action_4)


task2.depends_on(task0)
task3.depends_on(task1)
task3.depends_on(task2)
task4.depends_on(task3)

taskgraph = task.Taskgraph()
taskgraph.append_task(task3)
taskgraph.append_task(task2)
taskgraph.append_task(task0)
taskgraph.append_task(task1)
taskgraph.append_task(task4)

taskgraph.run_in_threads()
