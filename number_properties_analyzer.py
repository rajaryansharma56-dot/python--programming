print("\n ==== NUMBER  PROPERTIES USING LOOPS ====  ")

n=int(input("enter a number :"))

sum_even_digit=0
sum_odd_digit=0

count=0

rev_num=0
original=n

while(n>0):
    digit=n%10
    count=count+1

    if digit%2==0:
        sum_even_digit=sum_even_digit+digit

    else:
        sum_odd_digit=sum_odd_digit+digit

    rev_num=rev_num*10+digit

    n=n//10

if original==rev_num:
    print("palindrome ")

else:
    print("not a palindrome")


print("Number of digits:", count)
print("Sum of even digits:", sum_even_digit)
print("sum of odd digits:", sum_odd_digit)
print("Reversed number:", rev_num)



    

    

    

    

    
