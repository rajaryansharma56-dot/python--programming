even_num_count=0

odd_num_count=0

total_sum=0

sum_even_num=0

sum_odd_num=0


  
for i in range(1,11):
    
    n=int(input(f"enter number{i} :"))

    if n%2==0:
     even_num_count+=1
     sum_even_num +=n
    else:
     odd_num_count+=1
     sum_odd_num+=n

total_sum+=n


average_num=total_sum/10

print(f"even numbers are : {even_num_count}")
print(f"odd numbers are : {odd_num_count}")

print(f"sum of even numbers  : {sum_even_num}")
print(f"sum_odd_num  : {sum_odd_num}")
print(f"average of all 10 numbers is : {average_num}")
