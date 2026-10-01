print("\n ==== EXPENSE TRACKER ====\n")

total=0

highest_price=0
highest_item=" "




for i in range(1,6):
    item=input("enter the item name :")
    price=float(input("enter the item price :"))

    total+=price

    if price>highest_price:
        highest_price=price
        highest_item=item


average=total/5


print("\n ===== EXPENSE SUMMARY =====")

print("total expense :",total)
print("average expense :",average)
print("highest expense item :",highest_item,"with price :",highest_price)


print("\n ===== THANK YOU =====")
