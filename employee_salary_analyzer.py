"\n employee salary analizer "

n=int(input("enter number of employees  :"))

total_number_employees=n

employees_10_count=0
emloyees_5_count=0

for i in range(n):
    name=input("enter employee name :")
    basic_salary=float(input("enter basic salary :"))
    exp=int(input("enter experience years :"))

    if exp>=5:
        bonus=basic_salary*0.1
        employees_10_count+=1
    else:
        bonus=basic_salary*0.05
        emloyees_5_count+=1

    final_salary=basic_salary+bonus

    print("employee name :",name)
    print("basic salary :",basic_salary)
    print("bonus of employee :",bonus)
    print("final salary :",final_salary)

print("total number of employees :",total_number_employees)
print("number of employee receiving 10% Bonus are :",employees_10_count)
print("number of employee receiving 5% Bonus are :",emloyees_5_count)

print("\n ==== THANK YOU ====  ")
