class DataLayer:

    next_id = 1

    def __init__(self):
        self.__customers = []

    def create_customer(self, customer):
        id = DataLayer.next_id
        customer = [id, *customer] # * unpacks the customer variable
        self.__customers.append(customer)
        DataLayer.next_id += 1
        return customer

    def retrieve_customer(self, customer_id):
        for customer in self.__customers:
            if customer[0] == customer_id:
                return customer
        return None
    
    def retrieve_customers(self):
        return self.__customers