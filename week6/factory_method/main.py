# client side

from standard_devliery_factory import StandardDeliveryFactory
from express_delivery_factory import ExpressDeliveryFactory

def main():

    def process_delivery(factory):
        delivery = factory.create_delivery()
        delivery.process_delivery()

    standard_delivery_factory = StandardDeliveryFactory()
    process_delivery(standard_delivery_factory)

    express_delivery_factory = ExpressDeliveryFactory()
    process_delivery(express_delivery_factory)

if __name__ == '__main__':
    main()