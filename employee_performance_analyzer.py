
"\n Employee Performance Analyzer"

n = int(input("enter number of employee : "))

e_50_count = 0
highest_rating_count = 0
total_salary = 0

for i in range(n):

    name = input("enter employee name : ")
    basic_salary = int(input("enter basic salary of employee : "))
    exp_years = int(input("enter experience years : "))
    performance_rate = int(input("enter performance rating : "))

    # Experience bonus
    if exp_years < 2:
        bonus = basic_salary * 0.05

    elif exp_years <= 5:
        bonus = basic_salary * 0.10

    else:
        bonus = basic_salary * 0.15

    # Performance bonus
    if performance_rate == 5:
        additional_bonus = basic_salary * 0.10
        highest_rating_count += 1

    elif performance_rate == 4:
        additional_bonus = basic_salary * 0.05

    else:
        additional_bonus = 0

    # Salary calculation
    total_bonus = bonus + additional_bonus
    final_salary = basic_salary + total_bonus

    # Accumulate total salary
    total_salary += final_salary

    # Count employees with salary > 50000
    if final_salary > 50000:
        e_50_count += 1

    print(f"name and final salary : {name}, {final_salary}")


print(f"the total salary is : {total_salary}")
print(f"number of employees with final salary > 50000 : {e_50_count}")
print(f"number of employees who received the highest performance : {highest_rating_count}")
print("==== THANK YOU ====")
