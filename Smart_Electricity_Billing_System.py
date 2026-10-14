print("\n ==== ELECTRIC BILL CALCULATOR === ")

units=int(input("enter units consumed :"))

if units<=100:
    bill=units*2

elif units<=200:
    bill=100*2+(units-100)*3

else:
    bill=100*2+100*3+(units-200)*5


if bill<=300:
    print("LOW")

elif bill<=600:
    print("MEDIUM")

else:
    print("HIGH")

print(f"units consumed {units}:")
print(f"bill amount is {bill}:")
