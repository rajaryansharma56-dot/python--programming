# Multiplication Table Analyzer

n = int(input("Enter number: "))

table_sum = 0

for i in range(1, 11):
    result = n * i
    print(f"{n} × {i} = {result}")
    table_sum += result

print(f"\nSum of table: {table_sum}")
