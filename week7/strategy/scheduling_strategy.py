# Strategy Interface / Abstract class
from abc import ABC, abstractmethod

class SchedulingStrategy(ABC):

    @abstractmethod
    def schedule_tasks(self, tasks):
        pass