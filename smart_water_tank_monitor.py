current_level=int(input("enter current water level: "))

if current_level<0 and current_level>100:
    print("invalid input")

elif  current_level<=10:
    print("tank empty :",current_level)

elif  current_level<30:
    print("low water level",current_level)

elif current_level<=80:
    print("normal water level",current_level)

elif current_level<100:
    print("Tank almost full",current_level)

else:
    print("tank full:",current_level)
