"\n ==== number pattern analyzer ==== "

n = int(input("enter number of values : "))

positive_count = 0
negative_count = 0
zero_count = 0
even_count = 0
odd_count = 0
divisible_3_count = 0
prime_count = 0

total_sum = 0
largest_number = None
smallest_number = None

for i in range(n):

    number = int(input("enter number : "))

    # Positive / Negative / Zero

    if number > 0:
        positive_count += 1

    elif number < 0:
        negative_count += 1

    else:
        zero_count += 1

    # Even / Odd

    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    # Divisible by 3

    if number % 3 == 0:
        divisible_3_count += 1

    # Prime number

    if number > 1:

        prime = True

        for j in range(2, number):
            if number % j == 0:
                prime = False
                break

        if prime:
            prime_count += 1

    # Sum

    total_sum += number

    # Largest and smallest

    if largest_number is None or number > largest_number:
        largest_number = number

    if smallest_number is None or number < smallest_number:
        smallest_number = number


print("\n==== RESULT ====")

print(f"positive numbers : {positive_count}")
print(f"negative numbers : {negative_count}")
print(f"zeros : {zero_count}")
print(f"even numbers : {even_count}")
print(f"odd numbers : {odd_count}")
print(f"numbers divisible by 3 : {divisible_3_count}")
print(f"prime numbers : {prime_count}")
print(f"largest number : {largest_number}")
print(f"smallest number : {smallest_number}")
print(f"sum of all numbers : {total_sum}")

print("==== THANK YOU ====")
