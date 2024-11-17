from delivery_interface import Delivery

# concrete class
class ExpressDelivery(Delivery):

    def process_delivery(self):
        print("Processing express delivery.")