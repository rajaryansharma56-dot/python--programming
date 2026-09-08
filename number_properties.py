n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even number:", n)
else:
    print("Odd number:", n)

if n > 0:
    print("Positive number:", n)

    if n % 3 == 0:
        print("Divisible by 3:", n)

elif n < 0:
    print("Negative number:", n)
else:
    print("Zero")

print("\nEnd of program")
