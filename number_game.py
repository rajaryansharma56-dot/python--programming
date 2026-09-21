print("\n ==== NUMBER GAME ==== ")

a=int(input("enter value of a :"))
b=int(input("enter value of b :"))

sum=a+b
sub=a-b
multi=a*b


if(b!=0):

    div=a//b

    print("division :",div)

else:
    print("invalid input denominator cannot be zero :")

if sum>sub and sum>multi:
    print("largest result : Addition ")
elif sub>sum and sub>multi:
    print("largest result : subtraction ")

elif multi>sum and multi>sub:
    print("largest result : multiplication ")

else:
    print("there is a tie ")


print("\n ==== THANK YOU ==== ")

print("addition :",sum)
print("subtraction :",sub)
print("multiplication :",multi)
