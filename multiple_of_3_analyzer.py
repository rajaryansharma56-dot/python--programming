# Multiples Analyzer

div_num_count = 0
not_div_num_count = 0
sum_div_num = 0
largest_div_num = None

for i in range(1, 11):

    n = int(input(f"Enter number {i}: "))

    if n % 3 == 0:
        div_num_count += 1
        sum_div_num += n

        if largest_div_num is None or n > largest_div_num:
            largest_div_num = n

    else:
        not_div_num_count += 1

print(f"Numbers divisible by 3 : {div_num_count}")
print(f"Numbers not divisible by 3 : {not_div_num_count}")
print(f"Sum of numbers divisible by 3 : {sum_div_num}")
print(f"Largest number divisible by 3 : {largest_div_num}")

print("\n====== END OF CODE ======")
