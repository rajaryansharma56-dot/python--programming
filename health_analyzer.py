print("\n === HEALTH ANALYZER === ")

age=int(input("enter age of person :"))
weight=float(input("enter weight :"))
height=float(input("enter height :"))

if age<=0 or weight<=0 or height<=0:

    print("invalid input ")

else:

    bmi=weight/height**2

    print("BMI :",round(bmi,2))

    if bmi<18.5:
        print("category : Underweight")

    elif 18.5<=bmi<25:
        print("category : normal")

    elif 25<=bmi<30:
        print("category : overweight")

    else:
        print("category : obese")

    if age<18:
        print("age group : MINOR")

    else:
        print("age group : ADULT")

print("\n === THANK YOU ==== ")
