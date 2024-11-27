from tax_controller import TaxController
from tax_model import TaxModel
from tax_view import TaxView

def main():
    # Initialize Model, View, and Controller
    model = TaxModel()
    view = TaxView()
    controller = TaxController(model, view)

    # Simulate user input
    controller.add_income_entry(50000)
    controller.add_income_entry(30000)

    # Update and display tax summary
    controller.display_summary()


if __name__ == "__main__":
    main() # ERROR = AttributeError: 'TaxController' object has no attribute 'update'