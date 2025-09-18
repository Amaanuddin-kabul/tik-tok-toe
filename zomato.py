class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    # Deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive.")

    # Withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance! Transaction failed.")
        else:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. Remaining balance: ₹{self.balance}")

    # Check balance
    def check_balance(self):
        print(f"Account Balance: ₹{self.balance}")

    # Display account info
    def display_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ₹{self.balance}")


# Example Usage
if __name__ == "__main__":
    # Create a bank account
    account1 = BankAccount(101, "Amaan Uddin", 5000)

    account1.display_info()       # Show account details
    account1.deposit(2000)        # Deposit money
    account1.withdraw(1500)       # Withdraw money
    account1.withdraw(6000)       # Trying to withdraw more than balance
    account1.check_balance()      # Check balance
