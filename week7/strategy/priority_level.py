# Concrete Strategy

from scheduling_strategy import SchedulingStrategy

class PriorityLevelStrategy(SchedulingStrategy):
    
    def schedule_task(self, tasks):
        print("Scheduling tasks using Priority Level Strategy...")
        sorted_tasks = sorted(tasks, key=lambda x: x["priority"])
        for task in sorted_tasks:
            print(f"Task: Priority - {task['priority']}, Due Date - {task['due_date']}")