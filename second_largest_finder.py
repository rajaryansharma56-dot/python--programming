
print("\n === NUMBER ANALYZER === ")

n=int(input("enter no of numbers :"))

largest_num=None
second_largest_num=None



L=[]

for i in range(1,n+1):
    number=int(input(f"enter number {i}:"))
    L.append(number)



    if largest_num is None or number>largest_num:
        second_largest_num=largest_num
        largest_num=number

    elif number<largest_num and (second_largest_num is None or number>second_largest_num):
        second_largest_num=number

print(f"LARGEST NUMBER :  {largest_num}")

if second_largest_num is  None:
    print("NO SECOND LARGEST NUMBER")
else:
    print(f"SECOND LARGEST NUMBER : {second_largest_num}" )

print("\n === THANK YOU ===")
