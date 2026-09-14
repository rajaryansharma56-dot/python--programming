print("\n=== ATM SIMULATOR ===")

current_balance = 10000
withdrawal_amount = int(input("Enter withdrawal amount: "))

if withdrawal_amount <= 0:
    print("INVALID INPUT")

elif withdrawal_amount % 100 != 0:
    print("Amount must be a multiple of ₹100")

elif withdrawal_amount > current_balance:
    print("INSUFFICIENT BALANCE")

else:
    current_balance -= withdrawal_amount
    print("\nWithdrawal successful!")
    print(f"Withdrawal amount: ₹{withdrawal_amount}")
    print(f"Remaining balance: ₹{current_balance}")

print("\n==== THANK YOU ====")
