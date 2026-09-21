print("\n === CINEMA TICKET === ")

age=int(input("enter age :"))
movie=input("3D movie (Y/N) :").upper()


if age<=0:

    print("invalid input :")

else:
    if age<5:
        base_ticket=0
    elif 5<=age<=17:
        base_ticket=100
    elif 18<=age<=59:
        base_ticket=180

    else:
        base_ticket=120


    if movie=="Y":
        threeD_charge=50
    else:
        threeD_charge=0

    final_price=base_ticket+threeD_charge

    print("base ticket :" ,base_ticket)
    print("3D charge :, threeD_charge")
    print("final price :, final_price")

print("\n === THANK YOU === ")
