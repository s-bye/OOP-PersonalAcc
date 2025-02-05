from datetime import datetime
class Amount:
    def __init__(self, amount: float, transaction_type):
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = datetime.now()

    def __str__(self):
        return f"{self.transaction_type}: {self.amount} at {self.timestamp}"
