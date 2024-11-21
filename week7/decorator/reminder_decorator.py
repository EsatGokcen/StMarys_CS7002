# concrete decorator class
from task_decorator import TaskDecorator

class ReminderDecorator(TaskDecorator):
    def __init__(self, task, reminder_date):
        super().__init__(task)
        self._reminder_date = reminder_date

    def get_description(self):
        return super().get_description()

    def get_deadline(self):
        return super().get_deadline()

    def get_reminder(self):
        return self._reminder_date