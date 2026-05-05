# TODO: Import PaymentMethod class from paymentmethod.py
# Use: from paymentmethod import PaymentMethod
from paymentmethod import PaymentMethod

class PayPal(PaymentMethod):
    # TODO: Create __init__ method that accepts email parameter
    # and stores it as an instance attribute (self.email)
    def __init__(self, email):
        self.email = email
    
    # TODO: Implement process_payment(self, amount) method that:
    # - Returns a string in format: "Processing PayPal payment of $[amount]"
    def process_payment(self, amount):
        return f"Processing PayPal payment of ${amount}"
    
    # TODO: Implement payment_details(self) method that:
    # - Returns a string in format: "PayPal account: [email]"
    def payment_details(self):
        return f"PayPal account: {self.email}"

