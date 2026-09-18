"\n ==== parking management calculator ==== "

n = int(input("enter total number of vehicles :"))

total_vehicles_count = 0
total_bikes_count = 0
total_cars_count = 0
total_trucks_count = 0
total_revenue = 0
number_vehicles_penalty = 0
vechicle_highest_charge = None

for i in range(n):

    vehicle_number = input("Enter vehicle number: ")
    vehicle_type = input("Enter vehicle type (B/C/T): ")
    parking_hours = int(input("Enter parking hours: "))

    parking_charges = 0
    penalty = 0

    if vehicle_type == "B":
        total_bikes_count += 1

        if parking_hours <= 2:
            parking_charges = parking_hours * 20
        else:
            parking_charges = 2 * 20 + (parking_hours - 2) * 10

    elif vehicle_type == "C":
        total_cars_count += 1

        if parking_hours <= 2:
            parking_charges = parking_hours * 40
        else:
            parking_charges = 2 * 40 + (parking_hours - 2) * 20

    elif vehicle_type == "T":
        total_trucks_count += 1

        if parking_hours <= 2:
            parking_charges = parking_hours * 60
        else:
            parking_charges = 2 * 60 + (parking_hours - 2) * 30

    if parking_hours > 8:
        penalty = 100
        number_vehicles_penalty += 1

    final_parking_charges = parking_charges + penalty

    total_revenue += final_parking_charges
    total_vehicles_count += 1

    if vechicle_highest_charge is None or final_parking_charges > vechicle_highest_charge:
        vechicle_highest_charge = final_parking_charges
        highest_vehicle_number = vehicle_number
        highest_vehicle_type = vehicle_type

    print(f"vehicle number : {vehicle_number}")
    print(f"vehicle type : {vehicle_type}")
    print(f"parking hours : {parking_hours}")
    print(f"base parking charges : {parking_charges}")
    print(f"penalty : {penalty}")
    print(f"final parking charges : {final_parking_charges}")


print(f"total vehicles : {total_vehicles_count}")
print(f"total revenue : {total_revenue}")
print(f"total bikes : {total_bikes_count}")
print(f"total cars : {total_cars_count}")
print(f"total trucks : {total_trucks_count}")
print(f"number of vehicles getting penalty : {number_vehicles_penalty}")
print(f"vehicle which paid the highest parking charge : {highest_vehicle_number}, {highest_vehicle_type}, ₹{vechicle_highest_charge}")
print(f"==== THANK YOU ====")
