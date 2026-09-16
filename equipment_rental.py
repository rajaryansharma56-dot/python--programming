def rental_cost(hours,rate):
    basic_cost=hours*rate

    if basic_cost>1500:
        discount=basic_cost*0.1
    else:
        discount=0

    final_cost=basic_cost-discount

    return basic_cost,final_cost,discount

n=int(input("enter a number of equiment items"))

names=[]
final_costs=[]

total_revenue=0



for i in range(n):
    name=input("enter equiment name :")
    hours=float(input("enter number of hours :"))
    rate=float(input("enter rate per hour:"))

    basic_cost,final_cost,discount =rental_cost(hours,rate)

    print("\nEquipment:", name)
    print("Basic cost:", basic_cost)
    print("Discount:", discount)
    print("Final cost:", final_cost)



    names.append(name)
    final_costs.append(final_cost)

    total_revenue=total_revenue+final_cost

print("Total number of equipment:", n)
print("Total revenue:", total_revenue)
