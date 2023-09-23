
class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            return f"Deposited ${amount}. New balance: ${self._account_balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            return f"Withdrew ${amount}. New balance: ${self._account_balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount."

    def display_balance(self):
        return f"Account Balance for {self._account_holder_name}: ${self._account_balance}"


# Test the BankAccount class
if __name__ == "__main__":
    # Create a new BankAccount instance
    account = BankAccount("12345", "itachi uchihaclass BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            return f"Deposited ${amount}. New balance: ${self._account_balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            return f"Withdrew ${amount}. New balance: ${self._account_balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount."

    def display_balance(self):
        return f"Account Balance for {self._account_holder_name}: ${self._account_balance}"


# Test the BankAccount class
if __name__ == "__main__":
    # Create a new BankAccount instance
    account = BankAccount("12345", "John Doe", 1000)

    # Deposit and display balance
    print(account.deposit(500))
    print(account.display_balance())

    # Withdraw and display balance
    print(account.withdraw(200))
    print(account.display_balance())

    # Try to withdraw more than the balance
    print(account.withdraw(2000))
", 1000)

    # Deposit and display balance
    print(account.deposit(500))
    print(account.display_balance())

    # Withdraw and display balance
    print(account.withdraw(200))
    print(account.display_balance())

    # Try to withdraw more than the balance
    print(account.withdraw(2000))