print("/n SUM OF DIGITS THAT ARE EVEN ")

n=int(input("enter a number:"))

sum_even_digit=0

while n>0:
    digit=n%10

    if digit %2==0:
        sum_even_digit=sum_even_digit+digit

    n=n//10

print("sum of even digits:",sum_even_digit)
