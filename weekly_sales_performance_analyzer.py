print("\n === SALES PERFORMANCE ANALYZER === ")

sales_above_5000=0
sales_below_1000=0

highest_sales=None
lowest_sales=None

total_sales=0

for i in range(1,8):
    amount=int(input(f"enter sales amount {i}:"))

    total_sales=total_sales+amount

    if amount>5000:
        sales_above_5000=sales_above_5000+1

    if amount<1000:
        sales_below_1000=sales_below_1000+1

    if highest_sales is None or amount>highest_sales:
        highest_sales=amount

    if lowest_sales is None or amount<lowest_sales:
        lowest_sales=amount


   

average=total_sales/7

print("\n === WEEKLY SALES REPORT ===  ")

print(f"total weekly sales {total_sales}")
print(f"average sales {average}")
print(f"highest daliy sales {highest_sales}")
print(f"lowest daily sales {lowest_sales}")
print(f"days with sales above 5000 {sales_above_5000}")
print(f"days with sales below 1000 {sales_below_1000}")

if total_sales >= 30000:
    print("Performance: EXCELLENT")

elif total_sales >= 20000:
    print("Performance: GOOD")

else:
    print("Performance: NEEDS IMPROVEMENT")weekly_sales_performance_analyzer.py
