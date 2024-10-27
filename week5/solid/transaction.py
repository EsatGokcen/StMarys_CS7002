
class Transaction:

    next_transaction_id = 1000

    def __init__(self):
        self.__id = Transaction.next_transaction_id
        Transaction.next_transaction_id += 1
        self.__transactions = []

    def __repr__(self):
        return f'Transaction(id={self.__id})'
    
    def __str__(self):
        return f'Transaction id: {self.__id}'
    