print("\n==== RECURSIVR DIGIT SUM ====  ")

def sum_digit(n):
    if n==0:
        return 0
    else:
        return n%10+sum_digit(n//10)

num=int(input("enter a number :"))

result=sum_digit(num)

print(f"sum of digits is {result}")
