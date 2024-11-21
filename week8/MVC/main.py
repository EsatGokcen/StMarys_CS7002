from controller.stock_controller import StockController

def main():
    stock_controller = StockController()
    stock_controller.set_stock("Nvidia" , 150)

if __name__ == '__main__':
    main()