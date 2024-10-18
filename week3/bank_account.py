
class BankAccount():

    bank_name = "Esat Bank"
    next_account_id = 1000

    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder
        self.__balance = balance
        self.id = BankAccount.next_account_id 
        BankAccount.next_account_id += 1

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited £{amount}. New balance: £{self.__balance}.")

    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            print(f"Withdrew £{amount}. New balance: £{self.__balance}.")
        else:
            print("Insufficent funds!")

    def display_info(self):
        print(f"{self.bank_name}\nID: {self.id}\nBalance: £{self.__balance}\nHolder: {self.__account_holder}.")

if __name__ == "__main__":
    acc1 = BankAccount("Alice Khan",1000)
    acc2 = BankAccount("Bob Smith", 500)

    acc1.withdraw(200)
    acc2.deposit(200)
    acc1.withdraw(900)

    BankAccount.bank_name = "Esat Best Bank"

    acc1.display_info()
    acc2.display_info()