
rent_days=int(input("enter rent days "))

total_cost=0
discount=0

if rent_days<0:
    print("invalid input ")

else:
    if rent_days<=3:
        total_cost=rent_days*500

    elif 3<rent_days<=7:
        total_cost=3*500+(rent_days-3)*400

    else:
        total_cost=3*500+4*400+(rent_days-7)*300

    if total_cost>3000:
        discount=total_cost*0.1

    final_amount=total_cost-discount

    print(f"RENT DAYS {rent_days}")
    print(f"TOTAL COST {total_cost}")
    print(f"DISCOUNT OBTAINED {discount}")
    print(f"FINAL AMOUNT {final_amount}")
