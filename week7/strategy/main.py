# Client code
import datetime
from task_scheduler import TaskScheduler
from due_date_priority import DueDatePriorityStrategy
from shortest_duration import ShortestDurationStrategy
from priority_level import PriorityLevelStrategy

if __name__ == "__main__":
    tasks = [
        {"due_date": datetime.datetime(2022, 12, 31), "priority": "High", "duration": 2},
        {"due_date": datetime.datetime(2022, 10, 15), "priority": "Medium", "duration": 1},
        {"due_date": datetime.datetime(2022, 9, 30), "priority": "Low", "duration": 3},
    ]

    task_scheduler = TaskScheduler(DueDatePriorityStrategy())
    task_scheduler.schedule_tasks(tasks)

    print()

    task_scheduler.set_scheduling_strategy(PriorityLevelStrategy())
    task_scheduler.schedule_tasks(tasks)

    print()

    task_scheduler.set_scheduling_strategy(ShortestDurationStrategy())
    task_scheduler.schedule_tasks(tasks)