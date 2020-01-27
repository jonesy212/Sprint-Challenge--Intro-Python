# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels):
        self.num_wheels = num_wheels

    def drive(self):
        "Driving the car"
        return "Vrooom"

num_wheels = 4


# ground_vehicle = GroundVehicle(num_wheels)
# if ground_vehicle[Car]:
#     num_wheels = 4
#     print(f"The car has {self.num_wheels} wheels")
# else: 
#     if ground_vehicle[Motorcycle]:
#         num_wheels = 2
#         print(f"The Motorcycle has {self.num_wheels} wheels")

print(f"Most vehicles have {num_wheels} wheels and goes {self.GroundVehicle[drive}])
# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

# for vehicle in vehicles == GroundVehicle:

class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels, name,):
        super().__init__(num_wheels,)
        self.name = name

    def drive(self):
        return super().drive("BRAAAP!!").format
motorcycle = Motorcycle
if motorcycle:
    num_wheels = 2 

print(f"Motorcycles have {num_wheels} wheels and goes")

# vehicles = [
#     GroundVehicle(),
#     GroundVehicle(),
#     Motorcycle(),
#     GroundVehicle(),
#     Motorcycle(),
# ]

# # Go through the vehicles list and print the result of calling drive() on each.

# for vehicle in vehicles:
#     print(vehicle)
