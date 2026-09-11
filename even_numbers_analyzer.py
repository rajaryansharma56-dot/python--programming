even_count=0

sum_even_num=0

for i in range(1,11):
    n=int(input(f"enter number {i} :"))

    

    if n%2==0:
        even_count+=1
        sum_even_num+=n

    


print(f"even numbers are : {even_count}")

print(f"sum of all even numbers  are : {sum_even_num}")

print("\n ===== THANK YOU ===== ")
