number_people=int(input("enter no of people :"))

low_risk=0
medium_risk=0
high_risk=0


for i in range(number_people):
    weight=float(input("enter weight :"))
    height=float(input("enter height :"))
    blood_pressure=(input("enter blood_pressure :"))
    heart_rate=int(input("enter heart_rate :"))

    
   
    risk_count=0


    bmi=weight/(height**2)

    if bmi<18.5:
        print("LOW :")
    elif  bmi<=24.9:
        print("MEDIUM :")
    else:
        print("HIGH :")
        risk_count+=1


    if heart_rate<60:
        print("LOW :")
    elif  heart_rate<=100:
        print("MEDIUM :")
    else:
        print("HIGH :")

        risk_count+=1

    systolic, diastolic = map(int, blood_pressure.split("/"))

    if systolic < 90 or diastolic < 60:
        print("LOW")
    elif systolic <= 120 and diastolic <= 80:
        print("MEDIUM")
    else:
        print("HIGH")
        risk_count += 1

    if risk_count >= 2:
        print("Overall Risk: HIGH")
    elif risk_count == 1:
       print("Overall Risk: MEDIUM")
    else:
        print("Overall Risk: LOW")


print("\n===== SUMMARY REPORT =====")
print("Low Risk:", low_risk)
print("Medium Risk:", medium_risk)
print("High Risk:", high_risk)

print(f"==== THANK YOU ==== ")
