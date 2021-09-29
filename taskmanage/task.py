class Task:
    def __init__(self, name):
        self.name = name
        self.action = None
        self.dependencies = []

    def set_action(self, func):
        self.action = func

    def run(self):
        print(f"I am a task. My name is {self.name}")
        if self.action is not None:
            self.action()

    def depends_on(self, task):
        self.dependencies.append(task)


class Taskgraph:
    def __init__(self):
        self.tasks = []

    def append_task(self, task):
        self.tasks.append(task)

    def show_all_tasks(self):
        for t in self.tasks:
            print(t.name)

    def run(self):
        # TODO: take into account task dependencies
        for t in self.tasks:
            t.run()
