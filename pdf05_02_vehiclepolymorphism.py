## Defining the class "Vehicle"... ##
class Vehicle:

    def __init__(self, mpg, vin, reserved = False):
        self.mpg = mpg
        self.vin = vin
        self.reserved = reserved

    def isReserved(self):
        return self.reserved

    def getDescription(self):
        description = "MPG:" + str(self.mpg) + "    Vin:" + str(self.vin)
        return description

    def getType(self):
        return type(self).__name__

    def getVin(self):
        return self.vin

    def setReserved(self, reserved):
        self.reserved = reserved
        if reserved == True:
            return ("Vehicle {} is now reserved.".format(self.vin))
        elif reserved == False:
            return ("Vehicle {} is now unreserved.".format(self.vin))

## Defining the class "Van"... ##
class Van(Vehicle):
    def __init__(self, makeModel, mpg, numPassengers, vin):
        super().__init__(mpg, vin)
        self.makeModel = makeModel
        self.numPassengers = numPassengers

    def getDescription(self):
        description = super().getDescription() + "    Make Model:" + str(self.makeModel) + "    Num Passengers:" + str(self.numPassengers)
        return description

## Defining the class "Car"... ##
class Car(Vehicle):
    def __init__(self, makeModel, mpg, numPassengers, numDoors, vin):
        super().__init__(mpg, vin)
        self.makeModel = makeModel
        self.numPassengers = numPassengers
        self.numDoors = numDoors

    def getDescription(self):
        description = super().getDescription() + "    Make Model:" + str(self.makeModel) + "    Num Passengers:" + str(self.numPassengers) + "    Num Doors:" + str(self.numDoors)
        return description

## Defining the class "Truck"... ##
class Truck(Vehicle):
    def __init__(self, mpg, length, numRooms, vin):
        super().__init__(mpg, vin)
        self.length = length
        self.numRooms = numRooms

    def getDescription(self):
        description = super().getDescription() + "    Length:" + str(self.length) + "    Num Rooms:" + str(self.numRooms)
        return description

## Testing... ##
myVehicle = Vehicle(300, "MX300TBC")
assert myVehicle.mpg == 300
assert myVehicle.vin == "MX300TBC"
assert myVehicle.getType() == "Vehicle"
assert myVehicle.getDescription() == "MPG:300    Vin:MX300TBC"
assert myVehicle.isReserved() == False
assert myVehicle.setReserved(True) == "Vehicle MX300TBC is now reserved."

myCar = Car("Toyota", 300, 4, 6, "MX300TBC")
assert myCar.mpg == 300
assert myCar.vin == "MX300TBC"
assert myCar.numPassengers == 4
assert myCar.numDoors == 6
assert myCar.makeModel == "Toyota"
assert myCar.getType() == "Car"
assert myCar.getDescription() == "MPG:300    Vin:MX300TBC    Make Model:Toyota    Num Passengers:4    Num Doors:6"
assert myCar.isReserved() == False
assert myCar.setReserved(True) == "Vehicle MX300TBC is now reserved."

myVan = Van("Toyota", 300, 12, "MX300TBC")
assert myVan.mpg == 300
assert myVan.vin == "MX300TBC"
assert myVan.numPassengers == 12
assert myVan.makeModel == "Toyota"
assert myVan.getType() == "Van"
assert myVan.getDescription() == "MPG:300    Vin:MX300TBC    Make Model:Toyota    Num Passengers:12"
assert myVan.isReserved() == False
assert myVan.setReserved(True) == "Vehicle MX300TBC is now reserved."

myTruck = Truck(300, 12, 3, "MX300TBC")
assert myTruck.mpg == 300
assert myTruck.vin == "MX300TBC"
assert myTruck.length == 12
assert myTruck.numRooms == 3
assert myTruck.getType() == "Truck"
assert myTruck.getDescription() == "MPG:300    Vin:MX300TBC    Length:12    Num Rooms:3"
assert myTruck.isReserved() == False
assert myTruck.setReserved(True) == "Vehicle MX300TBC is now reserved."
