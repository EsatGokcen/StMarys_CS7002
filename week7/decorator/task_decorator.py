# decorator class

from task_interface import Task

class TaskDecorator(Task):
    def __init__(self, task):
        self._task = task

    def get_description(self):
        return self._task.get_description()

    def get_deadline(self):
        return self._task.get_deadline()