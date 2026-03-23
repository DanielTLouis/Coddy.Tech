# TODO: Import all required classes
from device import Device
from screen import Screen
from computer import Computer
from laptop import Laptop

def explain_mro(class_name):
    # TODO: Print the MRO (Method Resolution Order) for the given class
    # TODO: Format: "MRO for [class name]:" (note: NO space after the colon)
    # TODO: Use class_name.__name__ to get the name of the class
    # TODO: Use class_name.__mro__ to get the MRO tuple
    # TODO: Print each class name in the MRO on separate lines
    print(f"MRO for {Device.__name__}:")
    device_mro_list = Device.__mro__
    for i in device_mro_list:
        print(i.__name__)
    d = Device()
    print("Power on result:", d.power_on())
    print()

    print(f"MRO for {Screen.__name__}:")
    screen_mro_list = Screen.__mro__
    for i in screen_mro_list:
        print(i.__name__)
    s = Screen()
    print("Power on result:", s.power_on())
    print()

    print(f"MRO for {Computer.__name__}:")
    computer_mro_list = Computer.__mro__
    for i in computer_mro_list:
        print(i.__name__)
    c = Computer()
    print("Power on result:", c.power_on())
    print()

    print(f"MRO for {Laptop.__name__}:")
    laptop_mro_list = Laptop.__mro__
    for i in laptop_mro_list:
        print(i.__name__)
    l = Laptop()
    print("Power on result:", l.power_on())
    print()

    # TODO: Create an instance of the class
    # TODO: Call power_on() on the instance and store the result
    # TODO: Print: "Power on result: [result]"
    # TODO: Print an empty line for better readability
    


# Test your code
# TODO: Call explain_mro() with each class: Device, Screen, Computer, and Laptop
explain_mro("dummy")


