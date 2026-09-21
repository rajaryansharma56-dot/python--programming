print("\n === equipment rental === ")

days=int(input("enter number of rental  days :"))



original_cost=500*days

discount=0


if days<=0:
    print("invalid rental days :")

else:

   if 1<=days<=2:
    discount=0

   elif 3<=days<=5:
    discount=original_cost*0.1

   else:
    discount=original_cost*0.2

   final_cost=original_cost-discount


   print(f" original cost :{original_cost}")
   print(f"discount:{discount}")
   print(f"final amount :{final_cost}")

print("\n === thank you ===")
