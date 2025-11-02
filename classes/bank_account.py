
class BankAccount:
    def __init__(self, account_holder, initial_balance ):
        self.holder = account_holder
        self.balance = initial_balance

    def transfer_funds(self, other_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            other_account.balance += amount
            print("The transfer was successful.")
        else:
            print("amount error!!")

    def __str__(self):
        print(f"===Account details===\n"
              f"Account holder name: {self.holder}\n"
              f"Your account balance: {self.balance}")




