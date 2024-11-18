from delivery_factory import DeliveryFactory
from express_delivery import ExpressDelivery

class ExpressDeliveryFactory(DeliveryFactory):

    def create_delivery(self):
        return ExpressDelivery()