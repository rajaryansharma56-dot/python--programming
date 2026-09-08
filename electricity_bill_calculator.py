# electricity bill calculator

units=int(input("enter the number of units consumed :"))

if units<0:
    print("invalid input")
else:
    if units<=100:
        bill=units*2

    elif units<=200:
        bill=100*2 +(units-100)*3
    elif units<=400:

        
        bill=100*2 +100*3 +(units-200)*5
    else:
        bill=100*2 +100*3 +100*5 +(units-400)*7
print(f"the electricity bill is : {bill}")
