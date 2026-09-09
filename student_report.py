total_marks = 0
passed_students = 0
above_90_students = 0

highest_marks = None
lowest_marks = None

highest_student = ""
lowest_student = ""

for i in range(1, 11):

    name = input(f"Enter student {i} name: ")
    marks = int(input(f"Enter marks of {name}: "))

    total_marks += marks

    if marks >= 40:
        passed_students += 1

    if marks >= 90:
        above_90_students += 1

    if highest_marks is None or marks > highest_marks:
        highest_marks = marks
        highest_student = name

    if lowest_marks is None or marks < lowest_marks:
        lowest_marks = marks
        lowest_student = name

class_average = total_marks / 10

print("\n========== PERFORMANCE SUMMARY ==========")

print(f"Highest Marks   : {highest_marks}")
print(f"Highest Student : {highest_student}")

print(f"Lowest Marks    : {lowest_marks}")
print(f"Lowest Student  : {lowest_student}")

print(f"Passed Students : {passed_students}")
print(f"90+ Scorers     : {above_90_students}")

print(f"Class Average   : {class_average:.2f}")

print("=========================================")
