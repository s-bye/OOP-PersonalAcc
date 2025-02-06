# Personal Account Management 🏦

This project is a simple personal account management system. It allows you to create a personal account, deposit and withdraw money, and keep track of your transaction history.

## Features ✨

- Create a personal account with an account number and account holder name.
- Deposit money into the account.
- Withdraw money from the account.
- View transaction history.
- Get account details like balance, account number, and account holder name.
- Update account details.

## How to Use 🛠️    
1. **Create an Account**:
   ```python
   account = PersonalAccount(123456, "Your Name", 0, [])
   ```
    
2. **Deposit Money**:
    ```python
    account.deposit(Amount(100, "Deposit"))
    ```
    
3. **Withdraw Money**:
    ```python
    account.withdraw(Amount(50, "Withdraw"))
    ```
    
4. **View Transaction History**:
    ```python
    account.transaction_history()
    ```
    
5. **Get Account Details**:
    ```python
    print(account.get_balance())
    print(account.get_account_number())
    print(account.get_account_holder())
    ```
    
6. **Update Account Details**:
    ```python
    account.set_account_number(654321)
    account.set_account_holder("Your Name")
    ```
    
7. **Use Operators**: 
    ```python
    account + Amount(200, "Deposit")
    account - Amount(100, "Withdraw")
    ```

## UML Diagram 📊
![UML](https://i.ibb.co/Q3pQV799/UML-Pers-Acc.jpg)