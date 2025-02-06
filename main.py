from classes.Amount import Amount
from classes.Personal_Account import PersonalAccount

if __name__ == "__main__":
    account = PersonalAccount(123456, "Abai Nurlanov", 0, [])
    print(account)
    account.deposit(Amount(100, "Deposit"))
    account.withdraw(Amount(50, "Withdraw"))
    account.transaction_history()
    print(account.get_balance())
    print(account.get_account_number())
    print(account.get_account_holder())
    account.set_account_number(654321)
    account.set_account_holder("Baiastan Zamirbekov")
    print(account)
    account + Amount(200, "Deposit")
    account - Amount(100, "Withdraw")
    print(account)
    account.transaction_history()