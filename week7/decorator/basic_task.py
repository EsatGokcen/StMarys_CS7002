# Concrete Task Class
from task_interface import Task

class BasicTask(Task):
    def __init__(self, description, deadline):
        self._description = description
        self._deadline = deadline

    def get_description(self):
        return self._description

    def get_deadline(self):
        return self._deadline