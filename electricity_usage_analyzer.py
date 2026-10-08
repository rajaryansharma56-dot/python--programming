print("\n === ELECTRIC BILL ANALYZER ==== ")

n=int(input("enter number of months :"))

total_units=0
above_200=0
below_100=0

highest_monthly_usage=None

for i in range(1,n+1):


    month_units=int(input(f"enter units for month {i}:"))
    total_units=total_units+month_units

    if month_units>200:
        above_200=above_200+1
    elif month_units<100:
        below_100=below_100+1
    

    if highest_monthly_usage is None or month_units>highest_monthly_usage:
        highest_monthly_usage=month_units

average=total_units/n

print("\n ==== ELECTRIC BILL SUMMARY ====   ")
print("total units consumed:",total_units)
print("average units consumed:",average)
print("number of months above 200 units:",above_200)
print("number of months below 100 units:",below_100)
print("highest monthly usage:",highest_monthly_usage)

print("\n ==== THANK YOU =====  ")
