class DataLayer:

    def __init__(self):
        self.__customers = []

    def create_customer(self, customer):
        self.__customers.append(customer)

    def retrieve_customer(self, customer_id):
        for customer in self.__customers:
            if customer[0] == customer_id:
                return customer
        return None