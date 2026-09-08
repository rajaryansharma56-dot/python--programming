# bank account withdrawal program

account_balance=float(input("enter account balance :"))

withdrawal_amount=float(input("enter withdrawal amount :"))

if withdrawal_amount<=0:
    print("Invalid withdrawal amount :")

elif withdrawal_amount > account_balance:
    print("Insufficient balance :")

else:
    account_balance-=withdrawal_amount
    print(f"Withdrawal successful. New account balance: ₹{account_balance}")
print(f"amount withdrawn  :₹{withdrawal_amount}")
