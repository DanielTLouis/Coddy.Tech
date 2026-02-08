class BankAccount:
    # TODO: Add class attribute here
    bank_name = "Python National Bank"
    
    # TODO: Add the methods here
    def deposit(self, amount):
        self.balance += amount
        pass
    
    def withdraw(self, amount):
        self.balance -= amount
        pass
    
    def get_balance(self):
        return self.balance 
        pass
