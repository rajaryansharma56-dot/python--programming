print("\n === SUM OF EVEN AND ODD NUMBERS ===  ")

n=int(input("enter a  number :"))

sum_even_digit=0
sum_odd_digit=0

while(n>0):
    digit=n%10

    if digit%2==0:
        sum_even_digit=sum_even_digit+digit

    else:
        sum_odd_digit=sum_odd_digit+digit

    n=n//10

print("sum of even digits:",sum_even_digit)
print("sum of odd digits:",sum_odd_digit)


