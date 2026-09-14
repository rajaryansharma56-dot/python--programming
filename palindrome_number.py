"\n ==== PALINDROME CHECKING ==== "

n=int(input("enter a number :"))

original=n


rev_num=0

while(n>0):
    last_digit=n%10
    rev_num=rev_num*10+last_digit
    n=n//10

if(rev_num==original):
    print(" YES ,PALINDROME CONFIRMED :")

else:
    print("NOT A PALINDROMNE :")

print("\n ==== THANK YOU ====")
