
n = int(input("enter number of students : "))

passed_students_count = 0
students_75_count = 0
highest_marks = None
total_marks = 0
topper = None

for i in range(n):
    name = input("enter name of student : ")
    marks = int(input("enter marks of student : "))

    if marks >= 40:
        passed_students_count += 1

    if marks >= 75:
        students_75_count += 1

    if highest_marks is None or marks > highest_marks:
        highest_marks = marks
        topper = name

    total_marks += marks

average = total_marks / n

print(f"number of students : {n}")
print(f"number of passed students : {passed_students_count}")
print(f"students who scored 75 and above : {students_75_count}")
print(f"highest marks : {highest_marks}")
print(f"topper : {topper}")
print(f"average of students marks : {average:.2f}")

print("\n==== THANK YOU ====")
