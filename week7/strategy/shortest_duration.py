# Concrete Strategy

from scheduling_strategy import SchedulingStrategy

class ShortestDurationStrategy(SchedulingStrategy):

    def schedule_task(self, tasks):
        print("Scheduling tasks using Shortest Duration Strategy...")
        sorted_tasks = sorted(tasks, key=lambda x: x["duration"])
        for task in sorted_tasks:
            print(f"Task: Duration - {task['duration']} hours, Priority - {task['priority']}")