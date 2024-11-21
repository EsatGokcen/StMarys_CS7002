from custom_pizza_builder import CustomPizzaBuilder

def main():
    
    builder = CustomPizzaBuilder()
    builder.add_topping("Mushrooms")
    builder.add_topping("Peppers")
    builder.select_crust("Thin Crust")
    builder.choose_size("Large")
    pizza = builder.get_pizza()
    print("Custom Pizza:")
    print("Toppings:", pizza.toppings) # ERROR 'NoneType' object has no attribute 'toppings'
    print("Crust Type:", pizza.crust_type) # ERROR 'NoneType' object has no attribute 'crust_type'
    print("Size:", pizza.size) #ERROR 'NoneType' object has no attribute 'size'

if __name__ == '__main__':
    main()