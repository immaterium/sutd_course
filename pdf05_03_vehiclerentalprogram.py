# Authors: Yeo Yong Kiat & Lim Xuan Ping
# Date: 20 Jul 2018
# Running the Program:
# -The program has 9 modules (we left out the RentalAgencyUI and System Interface modules):
#     1. Reservations
#     2. Reservation
#     3. Vehicles
#     4. Vehicle
#     5. Car
#     6. Van
#     7. Truck
#     8. VehicleCosts
#     9. VehicleCost
# -We've written a user interface to "welcome" the user to our make-believe car
#  rental agency, and a loop that returns the user to the menu or for him/her to
#  exit.
# -To run this program, simply run the commandline "python vehicle_rental.py"

## Defining the class "VehicleCosts"... ##
class VehicleCosts:

    costs = {}

    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def getVehicleCost(self, vehicle_type):
        return self.costs[vehicle_type]


    def addVehicleCost(self, vehicle_type, vehicle_cost):
        self.costs.update({vehicle_type: vehicle_cost.getCosts()})

    def calcRentalCost(self, rental_days, rental_period, want_insurance, miles_driving):
       if rental_period == 'daily_rate':
           period_cost = (rental_days * self.costs[self.vehicle_type][rental_period])
       elif rental_period == 'weekly_rate':
           period_cost = (rental_days * (self.costs[self.vehicle_type][rental_period])/7)
       elif rental_period == 'weekend_rate':
           period_cost = (rental_days * (self.costs[self.vehicle_type][rental_period])/2)
       insurance_cost = ((self.costs[self.vehicle_type]['insurance_rate']) * want_insurance * rental_days)
       distance_cost = (miles_driving - self.costs[self.vehicle_type]['free_miles_per_day']) * (self.costs[self.vehicle_type]['per_mile_charge'])
       if distance_cost <= 0:
           distance_cost = 0
       else:
           distance_cost = distance_cost
       rental_cost = period_cost + insurance_cost + distance_cost
       return (round(period_cost,2), round(insurance_cost,2), round(distance_cost, 2), round(rental_cost,2))

## Defining the class "VehicleCost"... ##
class VehicleCost:

    def __init__(self, daily_rate, weekly_rate, weekend_rate, free_miles_per_day, per_mile_charge, insurance_rate):
        self.daily_rate = daily_rate
        self.weekly_rate = weekly_rate
        self.weekend_rate = weekend_rate
        self.free_miles_per_day = free_miles_per_day
        self.per_mile_charge = per_mile_charge
        self.insurance_rate = insurance_rate

    def getDailyRate(self):
        return self.daily_rate

    def getWeeklyRate(self):
        return self.weekly_rate

    def getWeekendRate(self):
        return self.weekend_rate

    def getMilesPerDay(self):
        return self.free_miles_per_day

    def getPerMileCharge(self):
        return self.per_mile_charge

    def getInsuranceRate(self):
        return self.insurance_rate

    def getCosts(self):
        return {'daily_rate': self.daily_rate, 'weekly_rate': self.weekly_rate, 'weekend_rate': self.weekend_rate, 'free_miles_per_day': self.free_miles_per_day, 'per_mile_charge': self.per_mile_charge, 'insurance_rate': self.insurance_rate}

## Defining the class "Reservations"... ##
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

## Defining the class "Reservation"... ##
class Reservation:

    def __init__(self, name, address, credit_card, vin):
        self.name = name
        self.address = address
        self.credit_card = credit_card
        self.vin = vin

## Defining the class "Vehicles"... ##
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
            return print ("Vehicle {} is now reserved.".format(self.vin))
        elif reserved == False:
                return print ("Vehicle {} is now unreserved.".format(self.vin))

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
#resv_1 = Reservation("Lim Xuan Ping", "River Valley Road", "4190 2400 3333 1234", "EJ5KU2435BE")
#resv_2 = Reservation("Yeo Yong Kiat", "Bishan Park", "4190 2400 3333 3333", "DK3KG8212UE")
#list_of_reservations = [resv_1, resv_2]

## Creating a vehicle aggregator... ##
myVehicles = Vehicles()

## Creating a reservation aggregator... ##
myReservations = Reservations(myVehicles)

## Loading all vehicles into myVehicles... ##
for veh in list_of_vehicles:
    myVehicles.addVehicle(veh)

## Loading all reservations into myReservation... ##
#for resv in list_of_reservations:
#    myReservations.addReservation(resv)

## Creating vehicle costs... ##
car_costs = VehicleCost(24.99, 180.00, 45.00, 100, 0.15, 14.99)
van_costs = VehicleCost(35.00, 220.00, 55.00, 0, 0.20, 14.99)
truck_costs = VehicleCost(34.95, 425.00, 110.00, 25, 0.25, 14.99)
vehicle_costs = {'Car': car_costs, 'Van': van_costs, 'Truck': truck_costs}

## Loading all vehicle costs into myVehicleCosts... ##
myVehicleCosts = VehicleCosts('Car')
for key,value in vehicle_costs.items():
    myVehicleCosts.addVehicleCost(key, value)

## Printing number of available vehicles... ##
# print()
# print ("Printing number of available vehicles...")
# print ("No of Cars = " + str(myVehicles.numAvailVehicles('Car')))
# print ("No of Vans = " + str(myVehicles.numAvailVehicles('Van')))
# print ("No of Trucks = " + str(myVehicles.numAvailVehicles('Truck')))
# print()
# print ("===========================================================")

## Printing list of available vehicles by Vin... ##
# print()
# print ("Printing list of available vehicles by Vin...")
# print ("List of Avail Cars:")
# print (myVehicles.getAvailVehicles('Car'))
# print()
# print ("List of Avail Vans:")
# print (myVehicles.getAvailVehicles('Van'))
# print()
# print ("List of Avail Trucks:")
# print (myVehicles.getAvailVehicles('Truck'))
# print()
# print ("===========================================================")

## Printing descriptions of available vehicles... ##
# print()
# print ("Printing description of vehicles by type...")
# print ("Description of Cars:")
# for each_car in myVehicles.allCars:
#     print (myVehicles.allCars[each_car].getDescription())
# print()
# print ("List of Avail Vans:")
# for each_van in myVehicles.allVans:
#     print (myVehicles.allVans[each_van].getDescription())
# print()
# print ("List of Avail Trucks:")
# for each_truck in myVehicles.allTrucks:
#     print (myVehicles.allTrucks[each_truck].getDescription())
# print()
# print ("===========================================================")

## Demonstrating how a van of Vin 'JK2RT8364HY' is reserved and then unreserved... ##
# print()
# print("Demonstrating how a van of Vin 'JK2RT8364HY' is reserved and then unreserved... ")
# print()
# print("Before reserving the van, the list of available vans is...")
# print (myVehicles.getAvailVehicles('Van'))
# myVehicles.reserveVehicle('JK2RT8364HY')
# print("After reserving the van, the list of available vans is...")
# print (myVehicles.getAvailVehicles('Van'))
# print("After unreserving the car, the list of available van is...")
# myVehicles.unreserveVehicle('JK2RT8364HY')
# print (myVehicles.getAvailVehicles('Van'))
# print()
# print ("===========================================================")

## Demonstrating how to get the Vin for reservations made under a credit card... ##
# print()
# print("Demonstrating how to get the Vin for reservations made under a credit card...")
# print()
# print ('4190 2400 3333 1234 reserved vehicle ' + myReservations.getVinforReserv('4190 2400 3333 1234'))
# print ('4190 2400 3333 3333 reserved vehicle ' + myReservations.getVinforReserv('4190 2400 3333 3333'))
# print()
# print ("===========================================================")

## Demonstrating how to get the Vin for reservations made under a credit card... ##
# print()
# print("Demonstrating how to get the Vin for reservations made under a credit card...")
# print()
# print ('4190 2400 3333 1234 reserved vehicle ' + myReservations.getVinforReserv('4190 2400 3333 1234'))
# print ('4190 2400 3333 3333 reserved vehicle ' + myReservations.getVinforReserv('4190 2400 3333 3333'))
# print()
# print ("===========================================================")

## Demonstrating how to add and cancel a reservation... ##
# print()
# print("Demonstrating how to add and cancel a reservation... ")
# print()
# print("Before Yvonne reserves a van, the list of available vans is...")
# print (myVehicles.getAvailVehicles('Van'))
# print()
# print("Yvonne now makes a reservation...")
# new_resv = Reservation("Yvonne Tan", "Bishan Park", "4190 2400 3333 1111", "JK2RT8364HY")
# myReservations.addReservation(new_resv)
# print("After Yvonne reserves a van, the list of available vans is...")
# print (myVehicles.getAvailVehicles('Van'))
# print()
# print("Yvonne now cancels her reservation...")
# myReservations.cancelReservation("Yvonne Tan", "Bishan Park")
# print("After Yvonne cancels her reservation, the list of available vans is...")
# print (myVehicles.getAvailVehicles('Van'))
# print ("===========================================================")

# Importing modules
import sys

while True:
    # Printing interactive surface console... #
    print ("Welcome to Yong Kiat's and Xuan Ping's Vehicle Rental Agency")
    print ("<<< MAIN MENU >>>")
    print ("1 - Display Vehicle Types")
    print ("2 - Check Rental Costs")
    print ("3 - Check Available Vehicles")
    print ("4 - Get Cost of Specific Rental")
    print ("5 - Make a Reservation")
    print ("6 - Cancel a Reservation")
    print ("7 - Quit")
    choice = input("Enter: ")
    print()

    if choice == "1":
        print ("Types of Vehicles Available for Rent:")
        print ("1 - Car")
        print ("2 - Van")
        print ("3 - Truck")
        print()
        next = input("Enter 1 to return to menu or 2 to exit: ")
        if next == "1":
            continue
        elif next == "2":
            sys.exit()

    elif choice == "2":
        print ("1 - Car")
        print ("2 - Van")
        print ("3 - Truck")
        choice = input("Enter Type of Vehicle: ")
        if choice == "1":
            print ("Rental Charges for Cars")
            dict = myVehicleCosts.getVehicleCost("Car")
            print ("Daily: " + str(dict['daily_rate']) +
            " Weekly: " + str(dict['weekly_rate']) +
            " Weekend: " + str(dict['weekend_rate']) +
            " Free Miles: " + str(dict['free_miles_per_day']) +
            " Per Mile Charge " + str(dict['per_mile_charge']) +
            " Daily Insurance: " + str(dict['insurance_rate']))
        elif choice == "2":
            print ("Rental Charges for Vans")
            dict = myVehicleCosts.getVehicleCost("Van")
            print ("Daily: " + str(dict['daily_rate']) +
            " Weekly: " + str(dict['weekly_rate']) +
            " Weekend: " + str(dict['weekend_rate']) +
            " Free Miles: " + str(dict['free_miles_per_day']) +
            " Per Mile Charge " + str(dict['per_mile_charge']) +
            " Daily Insurance: " + str(dict['insurance_rate']))
        elif choice == "3":
            print ("Rental Charges for Trucks")
            dict = myVehicleCosts.getVehicleCost("Truck")
            print ("Daily: " + str(dict['daily_rate']) +
            " Daily: " + str(dict['weekly_rate']) +
            " Weekend: " + str(dict['weekend_rate']) +
            " Free Miles: " + str(dict['free_miles_per_day']) +
            " Per Mile Charge " + str(dict['per_mile_charge']) +
            " Daily: " + str(dict['insurance_rate']))
        else:
            print ("Invalid input.")
        print()
        next = input("Enter 1 to return to menu or 2 to exit: ")
        if next == "1":
            continue
        elif next == "2":
            sys.exit()
        print()

    elif choice == "3":
        print ("1 - Car")
        print ("2 - Van")
        print ("3 - Truck")
        choice = input("Enter Type of Vehicle: ")
        if choice == "1":
            print ("Available Cars")
            for each_car in myVehicles.allCars:
                print (myVehicles.allCars[each_car].getDescription())
        elif choice == "2":
            print ("Available Vans")
            for each_van in myVehicles.allVans:
                print (myVehicles.allVans[each_van].getDescription())
        elif choice == "3":
            print ("Available Trucks")
            for each_truck in myVehicles.allTrucks:
                print (myVehicles.allTrucks[each_truck].getDescription())
        else:
            print ("Invalid input.")
        print()
        next = input("Enter 1 to return to menu or 2 to exit: ")
        if next == "1":
            continue
        elif next == "2":
            sys.exit()
        print()

    elif choice == "4":
        print ("1 - Car")
        print ("2 - Van")
        print ("3 - Truck")
        try:
            choice = input("Enter Type of Vehicle (1, 2 or 3): ")
            period = input("Enter Rental Period (daily_rate, weekly_rate, weekend_rate): ")
            days = float(input("How many days do you need the vehicle for: "))
            insure = input("Would you like insurance (Y/N): ")
            miles = float(input("Number of miles expected to drive: "))
            print ("ESTIMATED CAR RENTAL COST")
            if insure == "Y":
                insure = True
                print ("*You have opted for the daily insurance.")
            elif insure == "N":
                insure = False
                print ("*You have opted out of the daily insurance.")
        except:
            print ("One or more of your earlier inputs was invalid.")
        if choice == "1":
            myVehicleCosts = VehicleCosts('Car')
            print ("Daily rental for {} days would be ${}".format(days, myVehicleCosts.calcRentalCost(days, period, insure, miles)[0] + myVehicleCosts.calcRentalCost(days, period, insure, miles)[1]))
            print ("Your cost with an estimated mileage of {} would be ${}".format(miles, myVehicleCosts.calcRentalCost(days, period, insure, miles)[3]))
            print ("which includes 100 free miles and a charge of 0.15 per mile")
        elif choice == "2":
            myVehicleCosts = VehicleCosts('Van')
            print ("Daily rental for {} days would be ${}".format(days, myVehicleCosts.calcRentalCost(days, period, insure, miles)[0] + myVehicleCosts.calcRentalCost(days, period, insure, miles)[1]))
            print ("Your cost with an estimated mileage of {} would be ${}".format(miles, myVehicleCosts.calcRentalCost(days, period, insure, miles)[3]))
            print ("which includes 0 free miles and a charge of 0.20 per mile")
        if choice == "3":
            myVehicleCosts = VehicleCosts('Truck')
            print ("Daily rental for {} days would be ${}".format(days, myVehicleCosts.calcRentalCost(days, period, insure, miles)[0] + myVehicleCosts.calcRentalCost(days, period, insure, miles)[1]))
            print ("Your cost with an estimated mileage of {} would be ${}".format(miles, myVehicleCosts.calcRentalCost(days, period, insure, miles)[3]))
            print ("which includes 25 free miles and a charge of 0.25 per mile")
        print()
        next = input("Enter 1 to return to menu or 2 to exit: ")
        if next == "1":
            continue
        elif next == "2":
            sys.exit()
        print()

# return (period_cost, insurance_cost, distance_cost, rental_cost)

    elif choice == "5":
        print ("Enter Type of Vehicle:")
        print ("1 - Car")
        print ("2 - Van")
        print ("3 - Truck")
        choice = input("Enter: ")
        if choice == "1":
            veh_choice = "Car"
            print ("Available Cars")
            for each_car in myVehicles.allCars:
                print (myVehicles.allCars[each_car].getDescription())
        elif choice == "2":
            veh_choice = "Van"
            print ("Available Vans")
            for each_van in myVehicles.allVans:
                print (myVehicles.allVans[each_van].getDescription())
        elif choice == "3":
            veh_choice = "Truck"
            print ("Available Trucks")
            for each_truck in myVehicles.allTrucks:
                print (myVehicles.allTrucks[each_truck].getDescription())
        else:
            print ("Invalid input")
            print()
            next = input("Enter 1 to return to menu or 2 to exit: ")
            if next == "1":
                continue
            elif next == "2":
                sys.exit()
        vin_choice = input("Enter Vin of vehicle to reserve: ")
        if vin_choice not in myVehicles.getAvailVehicles(veh_choice):
            print ("This vehicle is not available for reservation.")
        else:
            myVehicles.reserveVehicle(vin_choice)
            name = input("Enter first and last name: ")
            address = input("Enter address: ")
            credit_card = input("Enter credit card number: ")
            resv = Reservation(name, address, credit_card, vin_choice)
            myReservations.addReservation(resv)
            print ("Reservation for vehicle {} made by {}".format(vin_choice, name))
            print()
        print()
        next = input("Enter 1 to return to menu or 2 to exit: ")
        if next == "1":
            continue
        elif next == "2":
            sys.exit()
        print()

    elif choice == "6":
        credit_card = input("Enter your credit card number: ")
        print ()
        print ("RESERVATION INFORMATION")
        try:
            for each_resv in myReservations.all_reservations:
                if credit_card == myReservations.all_reservations[each_resv].credit_card:
                    resv = each_resv
                    resv_vin = myReservations.all_reservations[each_resv].vin
            resv_object = myReservations.findReservation(myReservations.all_reservations[resv].name, myReservations.all_reservations[resv].address)
            print(resv_object.name + " " + resv_object.address)
            confirm = input("Confirm Cancellation (Y/N): ")
            if confirm == "Y":
                myReservations.cancelReservation(myReservations.all_reservations[resv].name, myReservations.all_reservations[resv].address)
            elif confirm == "N":
                print ("Your reservation is not cancelled.")
            print()
        except:
            print ("Your card has not been used to reserve any vehicle.")
        next = input("Enter 1 to return to menu or 2 to exit: ")
        print()
        if next == "1":
            continue
        elif next == "2":
            sys.exit()
        print()

    elif choice == "7":
        sys.exit()
