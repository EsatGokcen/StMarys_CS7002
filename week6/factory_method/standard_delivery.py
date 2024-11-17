from delivery_interface import Delivery

# concrete class
class StandardDelivery(Delivery):

    def process_delivery(self):
        print("Processing standard delivery.")