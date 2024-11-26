# Context: TaskScheduler

class TaskScheduler:
    def __init__(self, scheduling_strategy):
        self.scheduling_strategy = scheduling_strategy

    def set_scheduling_strategy(self, scheduling_strategy):
        self.scheduling_strategy = scheduling_strategy

    def schedule_tasks(self, tasks):
        self.scheduling_strategy.schedule_task(tasks)