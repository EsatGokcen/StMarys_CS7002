
# Modularity 

# is a software design principle that breaks a system into smaller, 
# self-contained modules, each handling a specific function. 
# These modules should be loosely coupled (minimal dependencies) 
# and highly cohesive (focused on a single task).

# Practice: rewrite below code using modularity 

class TaskManager:
    def __init__(self):
        self.__tasks = []
        self.__users = []

    def add_task(self, title, description, assigned_to=None):
        task = {"title": title, "description": description, "status": "New", "assigned_to": assigned_to}
        self.__tasks.append(task)

    def assign_task(self, task_title, user_name):
        for task in self.__tasks:
            if task["title"] == task_title: #checks value of key "title" in task dictionary
                task["assigned_to"] = user_name
                task["status"] = "Assigned"
                break

    def complete_task(self, task_title):
        for task in self.__tasks:
            if task["title"] == task_title:
                task["status"] = "Completed"
                break

    def display_tasks(self):
        for task in self.__tasks:
            print("Title:", task["title"])
            print("Description:", task["description"])
            print("Assigned To:", task["assigned_to"])
            print("Status:", task["status"])

    def add_user(self, name):
        self.__users.append(name)

# Usage
task_manager = TaskManager()
task_manager.add_user("Alice")
task_manager.add_user("Bob")
task_manager.add_task("Task 1", "Description 1", "Alice")
task_manager.assign_task("Task 1", "Bob")
task_manager.complete_task("Task 1")
task_manager.display_tasks()