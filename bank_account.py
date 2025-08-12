class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.__balance = int(balance)

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        self.__balance += amount

    def deposit(self, amount):
        if amount <= 0:
            raise Exception("Incorrect Deposit Amount")
        else:
            self.balance = amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = -amount
        else:
            raise Exception("Insufficient Balance")


jane = BankAccount("Jane", "1234", "3500")

print(jane.balance)
jane.deposit(500)
print(jane.balance)
jane.withdraw(500)
print(jane.balance)
