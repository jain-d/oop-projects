class Amount:
    def __init__(self, amount):
        try:
            self.__amount = int(amount)
        except ValueError:
            raise Exception("Numeral Value expected")

        if self.__amount <= 0:
            raise Exception("Incorrect Amount")

    @property
    def amount(self):
        return self.__amount

class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.__balance = int(balance)

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount: int):
        deposit_amount = Amount(amount)
        self.__balance += deposit_amount.amount

    def withdraw(self, amount):
        withdrawal_amount = Amount(amount)
        if withdrawal_amount.amount <= self.balance:
            self.__balance -= withdrawal_amount.amount
        else:
            raise Exception("Insufficient Balance")


jane = BankAccount("Jane", "1234", "3500")

print(jane.balance)
jane.deposit(500)
print(jane.balance)
jane.withdraw(500)
print(jane.balance)
