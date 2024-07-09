# OOP: Bank Account Example
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance
        self._history = []

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._history.append(f"Deposit: +{amount}")
        return self

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self._history.append(f"Withdrawal: -{amount}")
        else:
            print("Insufficient funds or invalid amount.")
        return self

    @property
    def balance(self):
        return self._balance

    def statement(self):
        print(f"Account: {self.owner} | Balance: ${self._balance}")
        for entry in self._history:
            print(f"  {entry}")

acc = BankAccount("Yasser", 500)
acc.deposit(200).withdraw(100)
acc.statement()
