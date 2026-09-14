print("\n=== Even, Odd, Largest, Smallest Number Calculator ===")

even_number_count = 0
odd_number_count = 0

sum_even_number = 0
sum_odd_number = 0

even_largest_number = None
odd_largest_number = None

even_smallest_number = None
odd_smallest_number = None

for i in range(1, 11):
    n = int(input(f"Enter number {i}: "))

    if n % 2 == 0:
        even_number_count += 1
        sum_even_number += n

        if even_largest_number is None or n > even_largest_number:
            even_largest_number = n

        if even_smallest_number is None or n < even_smallest_number:
            even_smallest_number = n

    else:
        odd_number_count += 1
        sum_odd_number += n

        if odd_largest_number is None or n > odd_largest_number:
            odd_largest_number = n

        if odd_smallest_number is None or n < odd_smallest_number:
            odd_smallest_number = n

print(f"\nEven numbers: {even_number_count}")
print(f"Odd numbers: {odd_number_count}")

print(f"Sum of even numbers: {sum_even_number}")
print(f"Sum of odd numbers: {sum_odd_number}")

print(f"Largest even number: {even_largest_number}")
print(f"Smallest even number: {even_smallest_number}")

print(f"Largest odd number: {odd_largest_number}")
print(f"Smallest odd number: {odd_smallest_number}")
