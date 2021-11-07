import threading
import time

class Taskgraph:
    def __init__(self):
        self.tasks = []
        self.run_sequence = []
        self.tasks_done = []

    def done(self, task):
        self.tasks_done.append(task)

    def append_task(self, task):
        self.tasks.append(task)
        task.done_callback = self.done

    def show_all_tasks(self):
        for t in self.tasks:
            print(t.name)

    def run_dumb(self):
        for t in self.tasks:
            t.run()

    def run_correct_order(self):
        tmp_tasks = set(self.tasks)
        while len(tmp_tasks) > 0:
            for t in set(tmp_tasks):
                if len(set(t.dependencies) & set(self.run_sequence)) == len(t.dependencies):
                    self.run_sequence.append(t)
                    tmp_tasks.remove(t)
        for t in self.run_sequence:
            t.run()

    def run(self):
        tmp_tasks = set(self.tasks)
        while len(self.tasks_done) < len(self.tasks):
            for t in set(tmp_tasks):
                if len(set(t.dependencies) & set(self.tasks_done)) == len(t.dependencies):
                    th = threading.Thread(name=t.name, target=t.run)
                    th.start()
                    tmp_tasks.remove(t)
            time.sleep(1)
