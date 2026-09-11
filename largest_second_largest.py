numbers=[]

for i in range(10):
    n=int(input(f"enter number {i+1}"))
    numbers.append(n)


largest=numbers[0]
smallest=numbers[0]

for n in numbers:
    if n>largest:
        largest=n
    if n<smallest:
        smallest=n

second_largest=None

for n in numbers:

    if n!=largest:
        if second_largest  is None or n>second_largest:
            second_largest=n

average=sum(numbers)/len(numbers)

print("Largest:", largest)
print("Second largest:", second_largest)
print("Smallest:", smallest)
print("Average:", average)
