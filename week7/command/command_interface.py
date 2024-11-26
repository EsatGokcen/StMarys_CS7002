from abc import ABC, abstractmethod

# Command: Command

class Command(ABC):
    
    @abstractmethod
    def execute(self):
        pass