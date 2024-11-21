from pizza_builder import PizzaBuilder
from pizza import Pizza

class PepperoniPizzaBuilder(PizzaBuilder):

    def __init__(self):
        self.toppings = []
        self.crust_type = None
        self.size = None

    def add_topping(self, topping):
        potential_toppings = ["pepperoni", "cheese", "tomato"]
        if topping in potential_toppings:
            self.toppings.append(topping)

    def select_crust(self, crust_type):
        self.crust_type = crust_type

    def choose_size(self, size):
        self.size = size

    def get_pizza(self):
        Pizza(self.toppings, self.crust_type, self.size) 