print("\n === palindrome check=== ")

n=int(input("enter a number :"))

original=n
rev_num=0

while(n>0):
    digit=n%10

    rev_num=rev_num*10+digit

    n=n//10


if original==rev_num:
    print("palindrome detected")
       
else:
    print("not a palindrome")
                          

print("number is ",rev_num)
