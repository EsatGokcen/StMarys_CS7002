
class Transaction:

    next_transaction_id = 1000

    def __init__(self):
        self.__id = Transaction.next_transaction_id
        Transaction.next_transaction_id += 1
    