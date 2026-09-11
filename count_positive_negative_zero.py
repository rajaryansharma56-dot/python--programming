#======<< program to count,postive,negative zero=======>>

postive_count=0

negative_count=0

zero_count=0

for i in range(1,11):
    n=int(input(f"enter number {i} :"))

    if n>0:
        positive_count+=1

    elif n==0:
        zero_count+=1
    else:
        negative_count+=1


print(f"postive numbers are : {positive_count}")
print(f"negative numbers are : {negative_count}")
print(f"zeroes are : {zero_count}")

print("\n  ===== end of code =====")
