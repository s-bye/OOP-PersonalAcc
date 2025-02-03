from classes.Amount import Amount
from classes.Personal_Account import PersonalAccount

if __name__ == "__main__":
    amount = Amount(1000, "Deposit")
    print(amount.amount)
    print(amount.transaction_type)
