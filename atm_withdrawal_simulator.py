print("\n === ATM WITHDRAWAL SIMULATOR ===  ")

balance=int(input("enter initial balance :"))
n=int(input("enter no of withdrawal attempts:"))

passed_count=0
falied_count=0

for i in range(1,n+1):
    amount=int(input(f"enter withdrawal amount{i}:"))

    if amount<=0:
        print("invalid withdrawal ")
        falied_count=falied_count+1

    elif amount>balance:
        print("insufficient balance")
        falied_count=falied_count+1

    else:
        balance=balance-amount
        passed_count=passed_count+1
        print("withdrawal successful")
        print("remaining balance:",balance)

print("\n ==== ATM SUMMARY ==== ")
print("final balance:",balance)
print("successful withdrawals:",passed_count)
print("failed withdrawals:",falied_count)

print("\n ==== THANK YOU ==== ")
