print("\n === SMART ENERGY METER ANALYZER === ")

total=0
over_10=0
highest_consumed=None

for i in range(1,8):
    daily=int(input(f"enter daily electricity consumptions {i}: "))
    

    total=total+daily

    if daily>10:
        over_10=over_10+1

    if highest_consumed is None or daily>highest_consumed:
        highest_consumed=highest_consumed+1

average=total/7

bill=total*8

print("\n === WEEKLY REPORT === ")
print("Total   consumption:", total, "kWh")
print("Average consumption:", average, "kWh")
print("Total electricity bill: Rs.",   bill)

print("Days above 10 kWh:", over_10)

print("Highest daily consumption:", highest_consumed, "kWh")

if total > 70:
    print("Warning: Weekly consumption exceeded 70 kWh")
else:
    print("Weekly consumption is within the limit")

