# Base Task Interface
from abc import ABC, abstractmethod

class Task(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_deadline(self):
        pass