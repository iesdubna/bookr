class Task:
    def __init__(self, name):
        self.name = name
        self.action = None
        self.dependencies = []
        self.done_queue = None

    def set_action(self, func):
        self.action = func

    def run(self):
        print(f"I am a task. My name is {self.name}")
        if self.action is not None:
            self.action()
        self.done_queue.put(self.name)

    def depends_on(self, task):
        self.dependencies.append(task.name)
