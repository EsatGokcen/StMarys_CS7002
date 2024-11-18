from delivery_factory import DeliveryFactory
from standard_delivery import StandardDelivery

class StandardDeliveryFactory(DeliveryFactory):

    def create_delivery(self):
        return StandardDelivery()