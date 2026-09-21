print("\n === parking fee calculator === ")

vehicle=input("enter vehicle type (C/B) :").upper()

hours=int(input("enter parking hours :"))



rate=0

if hours<=0:
    print("invalid parking hours  :")

elif vehicle!="C" and  vehicle!="B":
    print("invalid vehicle type :")

else:

    if vehicle=="B":
        if hours<=2:
            rate=20
        else:
            additional_hours=hours-2
            rate=20+additional_hours*10

    elif vehicle=="C":
        if hours<=2:
            rate=40
        else:
            additional_hours=hours-2
            rate=40+additional_hours*20


    if rate>100:
        surcharge=rate*0.10

    else:
        surcharge=0

    final_fee=rate+surcharge

    print("vehicle type :",vehicle)
    print("parking hours :",hours)
    print("basic fee :",rate)
    print("surcharge :",surcharge)
    print("final fee :",final_fee)

print("\n ==== THANK YOU =====")
