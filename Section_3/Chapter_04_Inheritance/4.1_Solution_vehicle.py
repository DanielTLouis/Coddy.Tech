class Vehicle:
    def __init__(self, make, model):
        # TODO: Initialize the Vehicle class with make and model parameters
        # TODO: Store make and model as instance attributes (self.make, self.model)
        self.make = make
        self.model = model
    
    def display_info(self):
        # TODO: Implement a display_info method that prints vehicle information
        # TODO: Print in format: "Vehicle: [make] [model]"
        # TODO: Use f-string formatting: f"Vehicle: {self.make} {self.model}"
        print(f"Vehicle: {self.make} {self.model}")
