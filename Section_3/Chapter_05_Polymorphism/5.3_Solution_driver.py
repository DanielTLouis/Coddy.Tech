from creditcard import CreditCard
from paypal import PayPal

# Test the implementations - DO NOT MODIFY THIS TEST CODE
cc = CreditCard("1234567890123456")
pp = PayPal("user@example.com")

# Process valid payments
if cc.validate(100):
    print(cc.process_payment(100))
    print(cc.payment_details())

if pp.validate(200):
    print(pp.process_payment(200))
    print(pp.payment_details())

# Try an invalid amount
if not pp.validate(0):
    print("Invalid payment amount")

# This would raise an error if uncommented:
# pm = PaymentMethod()  # Can't instantiate abstract class
