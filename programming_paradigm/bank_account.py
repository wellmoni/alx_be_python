class BankAccount:

    def __init__(self, initial_balance=0):

        self.__account_balance = initial_balance

    def deposit(self, amount):

        if amount>0:

            self.__account_balance = account_balance + amount

        else:
            raise ValueError("Deposit amount must be positive.")
    def withdraw(self, amount):

        if amount <=0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__account_balance:
         return False
        self.__account_balance = account_balance-amount
        return True

     def display_balance(self):

         print(f"Current Balance: ${self.__account_balance:.2f}")


