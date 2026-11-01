print("\n === STUDENT MARKS ANALYZER === \n")

n = int(input("Enter number of students: "))

highest_marks = None
lowest_marks = None

count_40 = 0
total_marks = 0

above_average = []
all_marks = []

for i in range(1, n + 1):
    marks = int(input(f"Enter marks of student {i}: "))

    all_marks.append(marks)
    total_marks += marks

    if highest_marks is None or marks > highest_marks:
        highest_marks = marks

    if lowest_marks is None or marks < lowest_marks:
        lowest_marks = marks

    if marks >= 40:
        count_40 += 1

if n > 0:
    average_marks = total_marks / n
else:
    average_marks = 0

for marks in all_marks:
    if marks > average_marks:
        above_average.append(marks)

print(f"\nHighest marks: {highest_marks}")
print(f"Lowest marks: {lowest_marks}")
print(f"Number of students with marks >= 40: {count_40}")
print(f"Total marks: {total_marks}")
print(f"Average marks: {average_marks:.2f}")
print(f"Number of students above average: {len(above_average)}")
print(f"Students scoring above average: {above_average}")
