class BankAccount:
    def __init__(self, iban):
        print("__init__ called.")
        self.iban = iban

    @staticmethod
    def validate(iban):
        return len(iban) == 20

numbers = ["88888888888888888888", "7777", "2222"]

for element in numbers:
    if BankAccount.validate(element):
        print(f"We can use {element} to create a bank account")
    else:
        print(f"The account number {element} is invalid")
