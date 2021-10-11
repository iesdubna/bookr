import time
from taskmanage import task


def open_door():
    print("Открыть дверь холодильника")
    

def elephant():
    time.sleep(2)
    print("Посмотреть на слона")
    time.sleep(2)
    print("Вытащить слона")
    
def giraffe():
    time.sleep(2)
    print("Посмотреть на жирафа")
    time.sleep(5)
    print("Положить жирафа")
def close_door():
    print("Закрыть дверь холодильника")
       
    

task0 = task.Task("0")
task0.set_action(open_door)

task1 = task.Task("1")
task1.set_action(elephant)

task2 = task.Task("2")
task2.set_action(giraffe)

task3 = task.Task("3")
task3.set_action(close_door)



task1.depends_on(task0)
task2.depends_on(task1)
task3.depends_on(task2)


taskgraph = task.Taskgraph()
taskgraph.append_task(task2)
taskgraph.append_task(task0)
taskgraph.append_task(task1)
taskgraph.append_task(task3)


#taskgraph.run_correct_order()
taskgraph.run_in_threads()
