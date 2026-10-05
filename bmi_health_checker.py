
print("\n === HEALTH RISK ANALYZER ===")

age=int(input("enter your age :"))
weight=float(input("enter your weight:"))
height=float(input("enter your height:"))

if age<=0 or weight<=0 or height<=0:
    print("invalid input")

else:
    bmi=weight/height**2

    if bmi<18.5:
        category="underweight"

    elif bmi<=24.9:
        category="normal"

    elif bmi<=29.9:
        category="overweight"

    else:
        category="obese"

    if bmi>=30 or age>=60:
        risk="HIGH RISK"

    elif bmi>=25 or age>=45:
        risk="MODERATE RISK"

    else:
        risk="LOW RISK"

    print("\n === HEALTH RISK ANALYZER ===")
    print(f"AGE: {age}")
    print(f"WEIGHT: {weight}")
    print(f"HEIGHT: {height}")
    print(f"BMI: {bmi:.2f}")
    print(f"CATEGORY: {category}")
    print(f"RISK: {risk}")

    print("\n ==== THANK YOU ====")
