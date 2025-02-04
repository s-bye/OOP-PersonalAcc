class PersonalAccount:
    def __init__(self, account_number:int, account_holder, balance:float, transactions:list):
        self.account_number = account_number
        self.account_holder = account_holder
        self._balance = balance
        self.transactions = transactions

    def deposit(self, amount):
        self._balance += amount.amount
        self.transactions.append(amount)
        print(f"Deposited {amount.amount} / Now your balance is {self._balance}")

    def withdraw(self, amount):
        self._balance -= amount.amount
        self.transactions.append(amount)
        print(f"Withdrew {amount.amount} / Now your balance is {self._balance}")

    def transaction_history(self):
        for transaction in self.transactions:
            print(f"{transaction.transaction_type}: {transaction.amount}")