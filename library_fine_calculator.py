print("\n ====== LIRARY FINE CALCULATOR =====  ")

name=input("enter student name :")
late_days=int(input("enter number of late days :"))

fine_per_day=0

total_fine=0

if late_days<0:
    print("invalid input ")

else:
    if late_days==0:
        fine_per_day=0

    elif 6<=late_days<=10:
        fine_per_day=2

    elif 6<=late_days<=10:
        fine_per_day=5


    else:
        fine_per_day=10

    total_fine=late_days*fine_per_day

    

    print("STUDENT NAME :",name)
    print("DAYS LATE :",late_days)
    print("FINE PER DAY :",fine_per_day)
    print("TOTAL FINE :",total_fine)


print("\n ===== THANK YOU ==== ")
