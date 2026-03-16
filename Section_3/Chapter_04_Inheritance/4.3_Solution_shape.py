import math

class Shape:
    def __init__(self, color):
        # TODO: Initialize the Shape class with color parameter
        # TODO: Store color as instance attribute (self.color)
        self.color = color
    
    def area(self):
        # TODO: Return 0 as a placeholder for child classes to override
        return 0
    
    def describe(self):
        # TODO: Print a description of the shape
        # TODO: Format should be exactly: "This is a {self.color} shape."
        print(f"This is a {self.color} shape.")
