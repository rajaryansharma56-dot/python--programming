def check_water(ph,turbidity):
    if 6.5<=ph<=8.5 and turbidity<3:
        return "Safe"

    else:
        return "Unsafe"

ph=float(input("enter ph level:"))
turbidity=int(input("enter turbidity:"))

result=check_water(ph,turbidity)

print("water quality:",result)
