from delivery_interface import Delivery

class StandardDelivery(Delivery):

    def process_delivery(self):
        print("Processing standard delivery.")