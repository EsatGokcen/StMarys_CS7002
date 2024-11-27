# Model

class TaxModel:
    
    def __init__(self):
        self.income_entries = []
        self.observers = []

    def add_income_entry(self, amount):
        self.income_entries.append(amount)
        self.notify_observers()

    def calculate_tax_liability(self):
        total_income = sum(self.income_entries)
        tax_liability = total_income * 0.20  # 20% tax rate in the UK
        return tax_liability

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()