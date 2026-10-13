print("\n === WEEKLY ELECTRIC ANALYZER  ===  ")

over_10=0
total=0
highest_daily_consumption=None

for i in range(1,8):
    units=int(input(f"enter units consumed {i}:"))

    total=total+units

    if units>10:
        over_10=over_10+1

    if highest_daily_consumption is None or units>highest_daily_consumption:
        highest_daily_consumption=units


average=total/7

if average>10:
    print("HIGH CONSUMPTION")

else:
    print("NORMAL CONSUMPTION")

print(f"total units cosumed  over 7 days {total}:")
print(f"number of days exceeding 10 units {over_10}:")
print(f"highest daily consumption {highest_daily_consumption}")
print(f"CATEGORY :AVERAGE COSUMPTION {average:.2f}:")

print("\n === THANK YOU ===  ")
