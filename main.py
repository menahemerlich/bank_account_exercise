from classes.bank_account import BankAccount

account1 = BankAccount("Erlich", 2500)
account2 = BankAccount("Etty", 3000)

account1.__str__()
account2.__str__()

account1.transfer_funds(account2, 500)

account1.__str__()
account2.__str__()



