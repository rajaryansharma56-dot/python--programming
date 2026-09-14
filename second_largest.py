numbers = []

largest_number = None
second_largest_number = None

for i in range(1, 11):
    n = int(input(f"Enter number {i}: "))

    numbers.append(n)

    if largest_number is None or n > largest_number:
        second_largest_number = largest_number
        largest_number = n

    elif second_largest_number is None or (n > second_largest_number and n != largest_number):
        second_largest_number = n

print(f"Largest number: {largest_number}")
print(f"Second largest distinct number: {second_largest_number}")
print(numbers)

print("\n===== THANK YOU =====")
