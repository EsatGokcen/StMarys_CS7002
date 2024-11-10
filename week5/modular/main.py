from task_manager import TaskManager

def main():

    task_manager = TaskManager()
    task_manager.add_user("Alice")
    task_manager.add_user("Bob")
    task1 = task_manager.add_task("Task 1", "Description 1")
    task_manager.assign_task(task1, "Bob")
    task_manager.complete_task(task1)
    task_manager.display_tasks()

if __name__ == '__main__':
    main()