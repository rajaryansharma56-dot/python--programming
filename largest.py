largest = None

for i in range(1, 11):
    n = int(input(f"Enter number {i}: "))

    if largest is None or n > largest:
        largest = n

print(f"\nLargest number is: {largest}")
