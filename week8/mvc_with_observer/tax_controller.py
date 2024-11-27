# Controller

class TaxController:
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.model.register_observer(self)

    def add_income_entry(self, amount):
        self.model.add_income_entry(amount)

    def display_summary(self):
        total_income = sum(self.model.income_entries)
        tax_liability = self.model.calculate_tax_liability()
        self.view.display_tax_summary(total_income, tax_liability)