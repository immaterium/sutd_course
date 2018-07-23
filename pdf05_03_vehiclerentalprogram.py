class Reservations:

    all_reservations = {}

    def __init__(self, vehicles):
        self.vehicles = vehicles

    def isReserved(self, vin):
        return self.vehicles.getVehicle(vin).isReserved()

    def findReservation(self, name, address):
        for each_resv in self.all_reservations:
            if (name, address) == (each_resv[0], each_resv[1]):
                found_resv = each_resv
        return self.all_reservations[found_resv]

    def cancelReservation(self, name, address):
        for each_resv in self.all_reservations:
            if (name, address) == (each_resv[0], each_resv[1]):
                cancelled_resv = each_resv
                self.vehicles.unreserveVehicle(self.all_reservations[cancelled_resv].vin)
        del self.all_reservations[cancelled_resv]


    def addReservation(self, resv):
        self.all_reservations[(resv.name, resv.address, resv.credit_card)] = resv
        try:
            self.vehicles.reserveVehicle(resv.vin)
            print ("New reservation made by {} for vehicle {}".format(resv.name, resv.vin))
        except:
            pass

    def getVinforReserv(self, credit_card):
        for key in self.all_reservations:
            if credit_card == key[2]:
                reserved_key = key
                return self.all_reservations[reserved_key].vin

class Reservation:

    def __init__(self, name, address, credit_card, vin):
        self.name = name
        self.address = address
        self.credit_card = credit_card
        self.vin = vin

class Vehicles:

    availCars = {}
    availTrucks = {}
    availVans = {}
    availVehicles = {}
    allCars = {}
    allTrucks = {}
    allVans = {}
    allVehicles = {}

    def unreserveVehicle(self, vin):
        for each_vin in self.allVehicles:
            if each_vin == vin:
                unreserved_vin = each_vin
                self.allVehicles[each_vin].setReserved(False)
                if self.allVehicles[each_vin].getType() == "Car":
                    self.availCars[each_vin] = self.allVehicles[each_vin]
                if self.allVehicles[each_vin].getType() == "Truck":
                    self.availTrucks[each_vin] = self.allVehicles[each_vin]
                if self.allVehicles[each_vin].getType() == "Van":
                    self.availVans[each_vin] = self.allVehicles[each_vin]
        self.availVehicles[unreserved_vin] = self.allVehicles[unreserved_vin]

    def reserveVehicle(self, vin):
        for each_vin in self.availVehicles:
            if each_vin == vin:
                reserved_vin = each_vin
                self.availVehicles[each_vin].setReserved(True)
                if self.availVehicles[each_vin].getType() == "Car":
                    del self.availCars[each_vin]
                elif self.availVehicles[each_vin].getType() == "Van":
                    del self.availVans[each_vin]
                elif self.availVehicles[each_vin].getType() == "Truck":
                    del self.availTrucks[each_vin]
        del self.availVehicles[reserved_vin]

    def getVehicle(self, vin):
        for each_vin in self.allVehicles:
            if each_vin == vin:
                return self.allVehicles[each_vin]

    def numAvailVehicles(self, vehicle_type):
            return len(self.getAvailVehicles(vehicle_type))

    def getAvailVehicles(self, vehicle_type):
        if vehicle_type == 'Car':
            return [each_vin for each_vin in self.availCars]
        if vehicle_type == 'Van':
            return [each_vin for each_vin in self.availVans]
        if vehicle_type == 'Truck':
            return [each_vin for each_vin in self.availTrucks]

    def addVehicle(self, vehicle):
        if vehicle.getType() == 'Car':
            self.allCars[vehicle.getVin()] = vehicle
            self.allVehicles[vehicle.getVin()] = vehicle
            self.availCars[vehicle.getVin()] = vehicle
            self.availVehicles[vehicle.getVin()] = vehicle
            for each_vin in self.allCars:
                if self.allCars[each_vin].isReserved() == False:
                    self.availCars[each_vin] = self.allCars[each_vin]
                else:
                    continue
        elif vehicle.getType() == 'Van':
            self.allVans[vehicle.getVin()] = vehicle
            self.allVehicles[vehicle.getVin()] = vehicle
            self.availVans[vehicle.getVin()] = vehicle
            self.availVehicles[vehicle.getVin()] = vehicle
            for each_vin in self.allVans:
                if self.allVans[each_vin].isReserved() == False:
                    self.availVans[each_vin] = self.allVans[each_vin]
                else:
                    continue
        elif vehicle.getType() == 'Truck':
            self.allTrucks[vehicle.getVin()] = vehicle
            self.allVehicles[vehicle.getVin()] = vehicle
            self.availTrucks[vehicle.getVin()] = vehicle
            self.availVehicles[vehicle.getVin()] = vehicle
            for each_vin in self.allTrucks:
                if self.allTrucks[each_vin].isReserved() == False:
                    self.availTrucks[each_vin] = self.allTrucks[each_vin]
                else:
                    continue

class Vehicle:

    def __init__(self, mpg, vin, reserved = False):
        self.mpg = mpg
        self.vin = vin
        self.reserved = reserved

    def isReserved(self):
        return self.reserved

    def getDescription(self):
        description = "MPG:" + str(self.mpg) + "\nVin:" + str(self.vin)
        return description

    def getType(self):
        return type(self).__name__

    def getVin(self):
        return self.vin

    def setReserved(self, reserved):
        self.reserved = reserved
        if reserved == True:
            return print ("Vehicle {} is now reserved.".format(self.vin))
        elif reserved == False:
                return print ("Vehicle {} is now unreserved.".format(self.vin))

class Van(Vehicle):
    def __init__(self, makeModel, mpg, numPassengers, vin):
        super().__init__(mpg, vin)
        self.makeModel = makeModel
        self.numPassengers = numPassengers

    def getDescription(self):
        description = super().getDescription() + "\nMake Model:" + str(self.makeModel) + "\nNum Passengers:" + str(self.numPassengers)
        return description

class Car(Vehicle):
    def __init__(self, makeModel, mpg, numPassengers, numDoors, vin):
        super().__init__(mpg, vin)
        self.makeModel = makeModel
        self.numPassengers = numPassengers
        self.numDoors = numDoors

    def getDescription(self):
        description = super().getDescription() + "\nMake Model:" + str(self.makeModel) + "\nNum Passengers:" + str(self.numPassengers) + "\nNum Doors:" + str(self.numDoors)
        return description

class Truck(Vehicle):
    def __init__(self, mpg, length, numRooms, vin):
        super().__init__(mpg, vin)
        self.length = length
        self.numRooms = numRooms

    def getDescription(self):
        description = super().getDescription() + "\nLength:" + str(self.length) + "\nNum Rooms:" + str(self.numRooms)
        return description

## Creating vehicles... ##
veh_1 = Car('Chevrolet Camaro', '30', '4', '2', 'WG8JM5492DY')
veh_2 = Car('Chevrolet Camaro', '30', '4', '2', 'KH4GM4564GD')
veh_3 = Car('Ford Fusion', '34', '5', '4', 'AB4FG5689GM')
veh_4 = Car('Ford Fusion Hybrid', '35', '5', '4', 'GH2KL4278TK')
veh_5 = Car('Ford Fusion Hybrid', '35', '5', '4', 'KU4EG3245RW')
veh_6 = Car('Chevrolet Impala', '36', '6', '4', 'QD4PK7394JI')
veh_7 = Van('Chrysler Town&Country', '25', '7', 'DK3KG8212UE')
veh_8 = Van('Chrysler Town&Country', '25', '7', 'VM9RE2645TD')
veh_9 = Van('Chrysler Town&Country', '25', '7', 'WK8BF4287DX')
veh_10 = Van('Dodge Caravan', '25', '7', 'KY8EW2053XT')
veh_11 = Van('Dodge Caravan', '25', '7', 'QK3FL4278ME')
veh_12 = Van('Ford Expedition', '20', '8', 'JK2RT8364HY')
veh_13 = Van('Ford Expedition', '20', '8', 'KH4ME4216XW')
veh_14 = Truck('Ten-Foot', '12', '1 bedroom', 'EJ5KU2435BC')
veh_15 = Truck('Seventeen-Foot', '10', '2 bedrooms', 'EJ5KU2435BD')
veh_16 = Truck('Twenty Four-Foot', '8', '4 bedrooms', 'EJ5KU2435BE')
list_of_vehicles = [veh_1, veh_2, veh_3, veh_4, veh_5, veh_6, veh_7, veh_8, veh_9, veh_10, veh_11, veh_12, veh_13, veh_14, veh_15, veh_16]

## Creating reservations... ##
resv_1 = Reservation("Lim Xuan Ping", "River Valley Road", "4190 2400 3333 1234", "EJ5KU2435BE")
resv_2 = Reservation("Yeo Yong Kiat", "Bishan Park", "4190 2400 3333 3333", "DK3KG8212UE")
list_of_reservations = [resv_1, resv_2]

## Creating a vehicle aggregator... ##
myVehicles = Vehicles()

## Creating a reservation aggregator... ##
myReservations = Reservations(myVehicles)

## Adding all created vehicles into a list... ##
for veh in list_of_vehicles:
    myVehicles.addVehicle(veh)

## Adding all created reservations into a list... ##
for resv in list_of_reservations:
    myReservations.addReservation(resv)

## Printing number of available vehicles... ##
print()
print ("Printing number of available vehicles...")
print ("No of Cars = " + str(myVehicles.numAvailVehicles('Car')))
print ("No of Vans = " + str(myVehicles.numAvailVehicles('Van')))
print ("No of Trucks = " + str(myVehicles.numAvailVehicles('Truck')))
print()
print ("===========================================================")

## Printing list of available vehicles by Vin... ##
print()
print ("Printing list of available vehicles by Vin...")
print ("List of Avail Cars:")
print (myVehicles.getAvailVehicles('Car'))
print()
print ("List of Avail Vans:")
print (myVehicles.getAvailVehicles('Van'))
print()
print ("List of Avail Trucks:")
print (myVehicles.getAvailVehicles('Truck'))
print()
print ("===========================================================")

## Demonstrating how a van of Vin 'JK2RT8364HY' is reserved and then unreserved... ##
print()
print("Demonstrating how a van of Vin 'JK2RT8364HY' is reserved and then unreserved... ")
print()
print("Before reserving the van, the list of available vans is...")
print (myVehicles.getAvailVehicles('Van'))
myVehicles.reserveVehicle('JK2RT8364HY')
print("After reserving the van, the list of available vans is...")
print (myVehicles.getAvailVehicles('Van'))
print("After unreserving the car, the list of available van is...")
myVehicles.unreserveVehicle('JK2RT8364HY')
print (myVehicles.getAvailVehicles('Van'))
print()
print ("===========================================================")

## Demonstrating how to get the Vin for reservations made under a credit card... ##
print()
print("Demonstrating how to get the Vin for reservations made under a credit card...")
print()
print ('4190 2400 3333 1234 reserved vehicle ' + myReservations.getVinforReserv('4190 2400 3333 1234'))
print ('4190 2400 3333 3333 reserved vehicle ' + myReservations.getVinforReserv('4190 2400 3333 3333'))
print()
print ("===========================================================")

## Demonstrating how to get the Vin for reservations made under a credit card... ##
print()
print("Demonstrating how to get the Vin for reservations made under a credit card...")
print()
print ('4190 2400 3333 1234 reserved vehicle ' + myReservations.getVinforReserv('4190 2400 3333 1234'))
print ('4190 2400 3333 3333 reserved vehicle ' + myReservations.getVinforReserv('4190 2400 3333 3333'))
print()
print ("===========================================================")

## Demonstrating how to add and cancel a reservation... ##
print()
print("Demonstrating how to add and cancel a reservation... ")
print()
print("Before Yvonne reserves a van, the list of available vans is...")
print (myVehicles.getAvailVehicles('Van'))
print()
print("Yvonne now makes a reservation...")
new_resv = Reservation("Yvonne Tan", "Bishan Park", "4190 2400 3333 1111", "JK2RT8364HY")
myReservations.addReservation(new_resv)
print("After Yvonne reserves a van, the list of available vans is...")
print (myVehicles.getAvailVehicles('Van'))
print()
print("Yvonne now cancels her reservation...")
myReservations.cancelReservation("Yvonne Tan", "Bishan Park")
print("After Yvonne cancels her reservation, the list of available vans is...")
print (myVehicles.getAvailVehicles('Van'))
print ("===========================================================")

## Demonstra
