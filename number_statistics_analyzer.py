n = int(input("Enter number of values: "))

positive_count = 0
negative_count = 0
zero_count = 0
even_count = 0
odd_count = 0
divisible_count = 0
perfect_square_count = 0

positive_sum = 0
negative_sum = 0

largest = 0
smallest = 0

for i in range(n):
    number = int(input("Enter a number: "))

    if i == 0:
        largest = number
        smallest = number

    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

    if number > 0:
        print("Positive")
        positive_count += 1
        positive_sum += number
    elif number < 0:
        print("Negative")
        negative_count += 1
        negative_sum += number
    else:
        print("Zero")
        zero_count += 1

    if number % 2 == 0:
        print("Even")
        even_count += 1
    else:
        print("Odd")
        odd_count += 1

    if number % 3 == 0 and number % 5 == 0:
        print("Divisible by both 3 and 5")
        divisible_count += 1

    print("Square:", number * number)

    is_perfect_square = False

    if number >= 0:
        for j in range(number + 1):
            if j * j == number:
                is_perfect_square = True
                perfect_square_count += 1
                break

    if is_perfect_square:
        print("Perfect square")
    else:
        print("Not a perfect square")

print("Positive count:", positive_count)
print("Negative count:", negative_count)
print("Zero count:", zero_count)
print("Even count:", even_count)
print("Odd count:", odd_count)
print("Divisible by both 3 and 5:", divisible_count)
print("Positive sum:", positive_sum)
print("Negative sum:", negative_sum)
print("Largest:", largest)
print("Smallest:", smallest)
print("Perfect square count:", perfect_square_count)
