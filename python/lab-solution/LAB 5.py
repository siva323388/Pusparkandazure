# Step 1: Define Custom Exceptions

class InvalidAccountError(Exception):
    """Raised when an invalid account number is provided."""
    def __init__(self, message="Invalid account number provided"):
        self.message = message
        super().__init__(self.message)

class InsufficientBalanceError(Exception):
    """Raised when the account balance is insufficient for withdrawal."""
    def __init__(self, message="Insufficient balance for the withdrawal"):
        self.message = message
        super().__init__(self.message)

class InvalidAmountError(Exception):
    """Raised when the deposit or withdrawal amount is invalid (negative or zero)."""
    def __init__(self, message="Amount must be positive"):
        self.message = message
        super().__init__(self.message)

# Step 2: Create the BankAccount class
class BankAccount:
    def __init__(self, account_number, balance=0.0):
        if not account_number:
            raise InvalidAccountError("Account number cannot be empty")
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive")
        self.balance += amount
        print(f"Deposited {amount}. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise InsufficientBalanceError("Cannot withdraw more than the available balance")
        self.balance -= amount
        print(f"Withdrew {amount}. Current balance: {self.balance}")

    def get_balance(self):
        return self.balance

# Step 3: Main Program to simulate transactions
def main():
    try:
        # Create a BankAccount instance with a valid account number
        account = BankAccount("12345XYZ", 1000.0)
        
        # Perform some transactions
        account.deposit(500)
        account.withdraw(200)
        
        # Simulate error scenarios
        # account.deposit(-50)  # Invalid deposit
        # account.withdraw(1500)  # Insufficient balance
        account.withdraw(-100)  # Invalid withdrawal
        
    except InvalidAccountError as e:
        print(f"Invalid Account Error: {e}")
    except InsufficientBalanceError as e:
        print(f"Insufficient Balance Error: {e}")
    except InvalidAmountError as e:
        print(f"Invalid Amount Error: {e}")
    finally:
        print("Bank transaction completed.")

# Step 4: Run the main program
if __name__ == "__main__":
    main()
