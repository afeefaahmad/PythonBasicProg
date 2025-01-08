#Encapsulation : Bindidng data and code together 

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public attribute
        self._balance = balance               # Protected attribute
        self.__pin = 1234                     # Private attribute

    # Public method to access account details
    def get_account_details(self):
        return f"Account Number: {self.account_number}, Balance: {self._balance}"

    # Protected method to update balance
    def _update_balance(self, amount):
        self._balance += amount
        print(f"Updated Balance: {self._balance}")

    # Private method to validate PIN
    def __validate_pin(self, pin):
        return pin == self.__pin

    # Public method to withdraw money
    def withdraw(self, amount, pin):
        if self.__validate_pin(pin):  # Calling private method
            if amount <= self._balance:
                self._update_balance(-amount)  # Calling protected method
                print(f"Withdrawal successful. Amount: {amount}")
            else:
                print("Insufficient balance!")
        else:
            print("Invalid PIN!")

# Create an instance of BankAccount
account = BankAccount("123456789", 1000)

# Accessing public attribute
print(f"Account Number: {account.account_number}")  # Output: 123456789

# Accessing protected attribute (possible but discouraged)
print(f"Initial Balance: {account._balance}")  # Output: 1000

# Accessing private attribute (will cause an error if accessed directly)
# print(account.__pin)  # Uncommenting this line will raise an AttributeError

# Accessing private attribute using name mangling
print(f"PIN (via name mangling): {account._BankAccount__pin}")  # Output: 1234

# Withdrawing money using public method
account.withdraw(500, 1234)  # Output: Withdrawal successful. Amount: 500

# Trying to withdraw money with an invalid PIN
account.withdraw(300, 1111)  # Output: Invalid PIN!

