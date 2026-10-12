print("\n === PARKING CAPACIITY ANALYZER  ===  ")

capacity=int(input("enter parking capacity: "))

occupied=0

while True:
    choice=input("enter action (in/out/stop): ").lower()

    if choice=="in":
        if occupied<capacity:
            occupied=occupied+1
            print("vehicle parked")

        else:
            print("parking lot is full ")

    elif choice=="out":
        if occupied>0:
            occupied=occupied-1
            print("vehicle exited")
        else:
            print("parking lot is empty")

    elif choice=="stop":
        break

    else:
        print("invalid action")

print("occupied spaces:",occupied)
print("available spaces:",capacity-occupied)

print("\n ==== THANK YOU =====   ")
