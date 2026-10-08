n=int(input("enter number of transactions:"))

balance=0
total_money_add=0
total_money_spent=0
largest_trans_amount=None
largest_spending=0

for i in range(1,n+1):
    amount=int(input(f"enter transaction {i}:"))

    balance=balance+1

    if amount>0:
        total_money_add=total_money_add+amount

    elif amount<0:
        total_money_spent=total_money_spent+(-amount)

        if amount<-1000:
            largest_spending=largest_spending+1

    if largest_trans_amount is None or amount>largest_trans_amount:
        largest_trans_amount=amount


if balance>0:
    status="positive"

elif balance<0:
    status="negative"

else:
    status="zero"

print("total money received:",total_money_add)
print("total money spent:",total_money_spent)
print("largest transaction:",largest_trans_amount)
print("spending above 1000:",largest_spending)
print("status",status)
    
