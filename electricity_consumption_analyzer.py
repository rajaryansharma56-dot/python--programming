units = []

for i in range(7):
    x = int(input("Enter units for day " + str(i + 1) + ": "))
    units.append(x)

total = 0

for x in units:
    total = total + x

average = total / 7

highest = units[0]
lowest = units[0]

for x in units:
    if x > highest:
        highest = x

    if x < lowest:
        lowest = x

count = 0

for x in units:
    if x > average:
        count = count + 1

print("Total units:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Days above average:", count)
