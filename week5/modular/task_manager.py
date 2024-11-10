from task import Task
from user import User

class TaskManager:

    def __init__(self):
        self.__tasks = []
        self.__users = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.__tasks.append(task)

    def assign_task(self, task, user):
        task.assign_to_user(user)

    def complete_task(self, task):
        task.complete()

    def display_tasks(self):
        for task in self.__tasks:
            task.display_info()

    def add_user(self, name):
        user = User(name)
        self.__users.append(user)