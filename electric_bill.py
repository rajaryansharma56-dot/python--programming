print("\n ==== electric bill calculator ====  ")

units=int(input("enter number of units consumed :"))

bill=0

if units<=0:
    print("invalid input :")

else:

    if units<=100:
        bill=units*2
    elif units<=200:
        bill=100*2+(units-100)*3
    else:
        bill=100*2+200*3+(units-200)*5


    if bill>1000:
     surcharge=bill*0.05

    else:
     surcharge=0

final_bill=bill+surcharge


print(f"units consumed by the user :{units}")
print(f"bill :{bill}")
print(f"surcharge :{surcharge}")
print(f"final amount :{final_bill}")


print("\n  === THANK YOU === ")
