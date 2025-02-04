class Amount:
    def __init__(self, amount:float, transaction_type):
        self.amount = amount
        self.transaction_type = transaction_type
        print(f"Amount of {self.amount} created with transaction type {self.transaction_type}")