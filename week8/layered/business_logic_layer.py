class BusinessLogicLayer:

    def __init__(self, data_layer):
        self.__data_layer = data_layer

    def add_customer(self, customer):
        return self.__data_layer.create_customer(customer)
    
    def add_customers(self, customers):
        new_customers = []
        for customer in customers:
            new_customer = self.__data_layer.create_customer(customer)
            new_customers.append(new_customer)
        return new_customers

    def get_customer(self, id):
        self.__data_layer.retrieve_customer(id)

    def get_customers(self):
        return self.__data_layer.retrieve_customers()
        