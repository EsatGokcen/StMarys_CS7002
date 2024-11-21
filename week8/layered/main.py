from data_layer import DataLayer
from business_logic_layer import BusinessLogicLayer
from presentation_layer import PresentationLayer

def main():

    data_layer = DataLayer()
    business_logic = BusinessLogicLayer(data_layer)
    presentation = PresentationLayer(business_logic)

    customer1 = ["Esat", "Gokcen", "09/07/2001"]
    presentation.add_customer(customer1)
    presentation.display_all_customers()

if __name__ == '__main__':
    main()