camera=input("enter camera type :").lower()
days=int(input("enter number of days :"))
rate=float(input("enter rate per day :"))

total=days*rate
discount=0

if camera=="video":
    if total>1500:
        discount=total*0.12
elif camera=="drone":
    if total>2000:
        discount=total*0.15

else:
    print("invalid camera type :")
    exit()

final_cost=total-discount

print(f"original cost :{total}")
print(f"discount :{discount}")
print(f"final cost :{final_cost}")

print("\n ==== THANK YOU ====  ")
