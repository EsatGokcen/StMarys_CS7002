# interface

from abc import ABC, abstractmethod
class Delivery(ABC):

    @abstractmethod
    def process_delivery(self):
        pass