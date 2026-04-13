from vehicle import Vehicle
from car import Car
from motorcycle import Motorcycle
from truck import Truck

def vehicle_info(vehicle):
    return f"{vehicle.make} {vehicle.model}: {vehicle.start()}, Efficiency: {vehicle.fuel_efficiency()} mpg"


# Test with different vehicles - DO NOT MODIFY THIS TEST CODE
vehicles = [
    Car("Toyota", "Camry"),
    Motorcycle("Harley", "Davidson"),
    Truck("Ford", "F-150"),
    Vehicle("Generic", "Vehicle")
]

for v in vehicles:
    print(vehicle_info(v))
