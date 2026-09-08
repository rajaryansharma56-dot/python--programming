even_count = 0
odd_count = 0
even_sum = 0
odd_sum = 0

for i in range(1, 11):
    n = int(input(f"Enter number {i}: "))

    if n % 2 == 0:
        even_count += 1
        even_sum += n
    else:
        odd_count += 1
        odd_sum += n

print(f"\nEven numbers: {even_count}")
print(f"Odd numbers: {odd_count}")
print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")
