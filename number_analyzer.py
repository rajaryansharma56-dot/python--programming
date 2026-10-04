print("\n === NUMBER ANALYZER ===")

n=int(input("enter a number :"))

temp=n
count=0
total=0
largest=0

while temp>0:
    digit=temp%10

    count=count+1
    total=total+digit

    if digit>largest:
        largest=digit

    temp=temp//10


if n%2==0:
    print("Even")

else:
    print("odd")


print("Digits:",count)
print("Sum:",total)
print("Largest:",largest)
