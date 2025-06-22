class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the bank account with a balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit the specified amount."""
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw the specified amount if funds are sufficient."""
        if amount > 0 and self.account_balance >= amount:
            self.account_balance -= amount
            return True
        print("Insufficient funds or invalid amount.")
        return False

    def display_balance(self):
        """Print the current balance."""
        print(f"Current Balance: ${self.account_balance}")
