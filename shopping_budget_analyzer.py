print("\n ==== SHOPPING BUDGET ANALYZER ====")

total_cost=0
highest_price=0

for i in range(1,6):
    price=int(input(f"enter price of item {i}: "))
    total_cost+=price

    if price>highest_price:
        highest_price=price

average=total_cost/5

if total_cost<500:
    category="LOW SPENDING"

elif 500<=total_cost<=1500:
    category="MEDIUM SPENDING"

else:
    category="HIGH SPENDING"

print(f"total shopping cost : {total_cost}")
print(f"highest price : {highest_price}")
print(f"shopping average amount : {average}")
print(f"shopping spending category : {category}")

print("\n === THANK YOU ===")
