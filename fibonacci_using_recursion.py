def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


n=int(input("enter n: "))

if n<0:
    print("enter a non - negative number ")

else:
    print("fibonacci number ",fibonacci(n))
    
