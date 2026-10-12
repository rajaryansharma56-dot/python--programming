previous=float(input("enter consumption for hour 1:"))

for hour in range(2,7):
    current=float(input(f"enter consumption for hour{hour}:"))

    if previous>0 and current<previous*0.5:
        print(f"warning:suspicious consumption drop at hour{hour}")

    previous=currentr
