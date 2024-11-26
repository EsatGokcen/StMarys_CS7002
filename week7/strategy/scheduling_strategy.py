# Strategy Interface / Abstract class
from abc import ABC, abstractmethod

class SchedulingStrategy(ABC):

    @abstractmethod
    def schedule_task(self, tasks):
        pass