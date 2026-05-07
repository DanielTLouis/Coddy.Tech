# TODO: Import ABC and abstractmethod from abc module
from abc import ABC, abstractmethod

# Create the abstract base class
class PaymentMethod(ABC):
    # TODO: Create an abstract method process_payment(self, amount) using @abstractmethod decorator
    # This method should be declared but not implemented (use 'pass')
    @abstractmethod
    def process_payment(self, amount):
        pass

    # TODO: Create an abstract method payment_details(self) using @abstractmethod decorator
    # This method should be declared but not implemented (use 'pass')
    @abstractmethod
    def payment_details(self):
        pass

    # TODO: Create a concrete method validate(self, amount) that:
    # - Returns True if amount > 0
    # - Returns False otherwise
    def validate(self, amount):
        if amount > 0:
            return True
        else:
            return False

