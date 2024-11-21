# concrete task decorator
from task_decorator import TaskDecorator

class AttachmentDecorator(TaskDecorator):
    def __init__(self, task, attachment):
        super().__init__(task)
        self._attachment = attachment

    def get_description(self):
        return super().get_description()

    def get_deadline(self):
        return super().get_deadline()

    def get_attachment(self):
        return self._attachment