class PresentationLayer:

    def __init__(self, business_logic_layer):
        self.__business_logic_layer = business_logic_layer

    def display_all_customers(self):
        customers = self.__business_logic_layer.get_customers()
        print("id | first name | last name | date of birth")
        for customer in customers:
            print(f"{customer[0]:<4} | {customer[1]:<10} | {customer[2]:<10} | {customer[3]}")

    def add_customer(self):
        return self.__business_logic_layer.add_customer()
