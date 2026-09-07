#--------simple calcultor------#

print("n/---- SIMPLE CALCULATOR----/n")

n1=int(input("enter first number :"))
n2=int(input("enter second number :"))

op=input("enter operator(+,-,*,/,//,%,**):")

if op=='+':
    print("sum of two number is :",n1+n2)
elif op=='-':
    print("subtraction of two number is :",n1-n2)
elif op=='*':
    print("multiplication of two number is :",n1*n2)
elif op=='/':
    print("division of two number is :",n1/n2)
elif op=='//':
    print("floor division of two number is :",n1//n2)
elif op=='%':
    print("modulus of two number is :",n1%n2)
elif op=='**':
    print("exponentiation of two number is :",n1**n2)

else:
    print("INVALID OPERATOR :")

print("===== THANK YOU =====")
