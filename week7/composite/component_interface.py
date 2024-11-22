from abc import ABC, abstractmethod

# Component Interface
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def transform(self, transformation):
        pass