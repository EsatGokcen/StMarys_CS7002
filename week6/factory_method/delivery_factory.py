from abc import ABC, abstractmethod

class DeliveryFactory(ABC):

    @abstractmethod
    def create_delivery(self):
        pass