print("\n ==== TRANSACTION ANALYZER ====   ")

trans_no=int(input("enter number of transactions  :"))

total_trans_amount=0
highest_amount=None
lowest_amount=None

no_above_average=0
transaction=[]


for i in range(trans_no):
    amount=int(input("enter amount of transaction :"))
    transaction.append(amount)

    total_trans_amount=total_trans_amount+amount

    if highest_amount is None or amount>highest_amount:
        highest_amount=amount

    if lowest_amount is None or amount<lowest_amount:
        lowest_amount=amount

average=total_trans_amount/trans_no

for amount in transaction :
    if amount>average:
        no_above_average=no_above_average+1


print(f"no of transaction {trans_no}")
print(f"total transaction amount {total_trans_amount}")
print(f"highest transaction amount {highest_amount}")
print(f"lowest transaction amount {lowest_amount}")
print(f"number of transaction above average value is {no_above_average}")
print("\n ==== THANK YOU ====  ")
