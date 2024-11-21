class BusinessLogicLayer:

    def __init__(self, data_layer):
        self.__data_layer = data_layer

    def add_customer(self, customer):
        self.__data_layer.create_customer(customer)
    
    def add_customers(self, customers):
        for customer in customers:
            self.__data_layer.create_customer(customer)
        