print("second largest element")

n = int(input("enter number of elements: "))

largest = -999999
second = -999999

for i in range(n):
    num = int(input("enter number: "))

    if num > largest:
        second = largest
        largest = num

    elif num > second and num != largest:
        second = num

if second == -999999:
    print("second largest element does not exist")
else:
    print("second largest element:", second)
