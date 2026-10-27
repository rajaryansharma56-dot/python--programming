print("\n===== CALCULATOR =====")

while True:
    print("1.Addition ")
    print("2.Subtraction ")
    print("3.Divison ")
    print("4.Multiplication ")
    print("5.Exit")

    choice=int(input("enter your choice "))

    if(choice==5):
        print("invalid input/THANK YOU")
        break

    if choice not in (1, 2, 3, 4):
        print("Invalid input!")
        continue 

    num1=int(input("enter a number "))
    num2=int(input("enter a number "))

    if choice==1:
        print(f"ADDITION {num1+num2}")
    elif choice==2:
        print(f"SUBTRACTION {num1-num2}")
    elif choice==3:
        if num2==0:
            print("ERROR,GIVE ANOTHER NUMBER")
        else:
            print(f"DIVISION {num1/num2}")

    elif choice==4:
        print(f"MULTIPLICATION {num1*num2}")

print("thank you ")
    
