# Concrete Strategy

from scheduling_strategy import SchedulingStrategy

class DueDatePriorityStrategy(SchedulingStrategy):

    def schedule_task(self, tasks):
        print("Scheduling tasks using Due Date Priority Strategy...")
        sorted_tasks = sorted(tasks, key=lambda x: x["due_date"])
        for task in sorted_tasks:
            print(f"Task: Due Date - {task['due_date']}, Priority - {task['priority']}")