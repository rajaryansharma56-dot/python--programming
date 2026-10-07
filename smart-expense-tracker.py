print("\n ==== EXPENSE TRACKER ==== ")

n=int(input("enter number of expenses:"))

total_amount=0
highest_expense=None
lowest_expense=None

above_1000=0
below_1000=0

for i in range(1,n+1):
    expense_name=input(f"enter expense name{i}:")
    amount=int(input(f"enter amount{i}:"))

    total_amount=total_amount+amount

    if amount>=1000:
        above_1000=above_1000+1
    else:
        below_1000=below_1000+1

    if highest_expense is None or amount>highest_expense:
        highest_expense=amount

    if lowest_expense is None or amount<lowest_expense:
        lowest_expense=amount


average=total_amount/n

budget=int(input("enter budget amount:"))

if total_amount>budget:
    print("budget exceeded")
elif total_amount==budget:
    print("budget fully used ")
else:
    print("budget remaining")

print(f"total amount spent {total_amount}:")
print(f"average expense {average}")
print(f"highest expense {highest_expense}")
print(f"lowest expense {lowest_expense}")
print(f"budget {budget}")
print(f"expenses above or equal to 1000: {above_1000}")
print(f"expenses below 1000: {below_1000}")
print("\n ==== THANK YOU ==== ")
