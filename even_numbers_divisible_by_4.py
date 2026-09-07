
# Find numbers that are even and divisible by 4

number = int(input("Enter a number: "))

for i in range(1, number + 1):
    if i % 4 == 0:
        print(f"{i} is even and divisible by 4")

print("\n===== END OF PROGRAM =====")

