from model.stock_model import StockModel
from view.stock_view import StockView

class StockController:

    def __init__(self):
        self.__model = StockModel(name="Nvidia", price=100)
        self.__view = StockView(self.__model)

    def set_stock(self, name, price):
        self.__model.set_name(name)
        self.__model.set_price(price)

    def display_stock(self):
        self.__view.refresh()

    