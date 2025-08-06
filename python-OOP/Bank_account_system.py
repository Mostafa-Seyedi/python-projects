# Code to simulate a bank account using OOP

class BankAccount: 
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance



    def deposit(self, amount): 
        if amount > 0: 
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")   
        else: 
            print("Deposit amount must be positive.")
        
    
    def withdraw(self,amount): 
        if amount <= self.balance: 
            self.balance -= amount
            print(f"Wihdraw {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds.")


    def get_balance(self): 
        return self.balance

    def __str__(self): 
        return f"Account holder: {self.account_holder}\nBalance: {self.balance}"
    


# Usage example: 

if __name__ == "__main__": 
    account_holder = input("Enter the account holder's name: ")
    account = BankAccount(account_holder)

    # Print intial details 
    print(account)

    account.deposit(500)
    account.withdraw(200)
    account.deposit(400)

    print(f"Final balance: {account.get_balance()}")