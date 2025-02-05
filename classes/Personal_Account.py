from classes.Amount import Amount
class PersonalAccount:
    def __init__(self, account_number: int, account_holder, balance: float, transactions: list):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self._balance = 0
        self.transactions = transactions

    def deposit(self, amount):
        if amount < 0:
            print("Amount must be positive!")
            return
        transaction = Amount(amount, "Deposit")
        self._balance += amount.amount
        self.transactions.append(transaction)
        print(f"Deposited {amount.amount} | Now your balance is {self._balance}")

    def withdraw(self, amount):
        if amount > self._balance:
            print(f"Insufficient funds! Your balance is {self._balance}")
            return
        transaction = Amount(amount, "Withdraw")
        self._balance -= amount.amount
        self.transactions.append(transaction)
        print(f"Withdrew {amount.amount} | Now your balance is {self._balance}")

    def transaction_history(self):
        for transaction in self.transactions:
            print(f"- {transaction.transaction_type}: {transaction.amount}")

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, account_number: int):
        self.__account_number = account_number

    def get_account_holder(self):
        return self.__account_holder

    def set_account_holder(self, account_holder: str):
        self.__account_holder = account_holder

    def __str__(self):
        return f"Account number: {self.__account_number} | Account holder: {self.__account_holder} | Balance: {self._balance}"

    def __add__(self, amount):
        self.deposit(amount)
        return self

    def __sub__(self, amount):
        self.withdraw(amount)
        return self
