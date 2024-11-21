class PresentationLayer:

    def __init__(self, business_logic_layer):
        self.__business_logic_layer = business_logic_layer

    def display_all_customers(self):
        customers = self.__business_logic_layer.get_customers()
        print(f"{'id':<4} | {'first name':<10} | {'last name':<10} | date of birth")
        for customer in customers:
            print(f"{customer[0]:<4} | {customer[1]:<10} | {customer[2]:<10} | {customer[3]}")

    def add_customer(self, customer):
        return self.__business_logic_layer.add_customer(customer)
