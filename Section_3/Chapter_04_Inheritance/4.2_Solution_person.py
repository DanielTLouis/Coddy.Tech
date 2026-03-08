class Person:
    def __init__(self, name, age):
        # TODO: Initialize the Person class with name and age parameters
        # TODO: Store name and age as instance attributes (self.name, self.age)
        self.name = name
        self.age = age 
    
    def introduce(self):
        # TODO: Implement the introduce method that prints a greeting
        # TODO: Print exactly: "Hi, I'm [name] and I'm [age] years old"
        # TODO: Use f-string formatting with self.name and self.age
        print(f"Hi, I'm {self.name} and I'm {self.age} years old")
