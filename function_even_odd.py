# finding number is even or odd 

n=int(input("enter a number : "))

def even_odd(n):
    if n%2==0:
        print("number is even :",n)
    else:
        print("number is odd :",n)

print(even_odd(n))
