postive_num_count=0

negative_num_count=0

zeroes_count=0

sum_postive_count=0
sum_negative_count=0

for i in range(1,11):
    n=int(input(f"enter number : {i}"))

    if n>=1:
        postive_num_count+=1
        sum_postive_count+=n
    elif n==0:
        zeroes_count+=1
    else:
        negative_num_count+=1

        sum_negative_count+=n

print(f"even numbers are : {postive_num_count}")
print(f"negative numbers are : {negative_num_count}")
print(f"sum of postive numbers are :{sum_postive_count}")
print(f"sum of all numbers are : {sum_negative_count}")


print("\n ===== THANK YOU ======")


