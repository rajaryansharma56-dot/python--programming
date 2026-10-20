def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

n=int(input("enter a number :"))

if n<0:
    print("factorial is not a defined for negative numbers ")

else:
    print("factorial:",factorial(n))
