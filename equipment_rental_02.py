n=int(input("enter number of equiment :"))

total_revenue=0
discount_count=0

for i in range(n):
    name=input("enter name of equiment: ")
    hours_rent=float(input("enter rented hours of equiment :"))
    rate=float(input("enter rate of rent :"))

    basic_cost=hours_rent*rate

    if basic_cost>1500:
        discount=basic_cost*0.1
        discount_count+=1

    else:
        discount=0

    final_cost=basic_cost-discount
    total_revenue=total_revenue+final_cost

    print("\nEquipment:", name)
    print("Basic cost:", basic_cost)
    print("Discount:", discount)

    print("Final cost:", final_cost)

print("Total revenue:", total_revenue)
print("Equipment receiving discount:", discount_count)
