
class StockView:

    def __init__(self, stock_model):
        self.__stock_model = stock_model

    def refresh(self):
        print(f"Stock Name: {self.__stock_model.get_name()}")
        print(f"Stock Price: {self.__stock_model.get_price()}")
        
