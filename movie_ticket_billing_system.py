
"\n MOVIE TICKET BILLING SYSTEM"

n=int(input("enter number of customers :"))

total_revenue=0
total_tickets=0
discount_count=0

for i in range(n):

    name=input("enter customer name :")
    age=int(input("enter age :"))
    tickets=int(input("enter number of tickets :"))

    original_amount=tickets*200

    if age<12:
        discount=original_amount*0.5

    elif age<60:
        discount=0

    else:
        discount=original_amount*0.3

    final_amount=original_amount-discount

    total_revenue+=final_amount
    total_tickets+=tickets

    if discount>0:
        discount_count+=1

    print(f"customer name : {name}")
    print(f"final amount : {final_amount}")

print(f"total revenue : {total_revenue}")
print(f"total tickets sold : {total_tickets}")
print(f"customers who received discount : {discount_count}")

print("\n ==== THANK YOU ====")
