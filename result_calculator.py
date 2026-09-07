
# Student Grade Calculator

print("===== STUDENT GRADE CALCULATOR =====")

name = input("Enter student name: ")
roll_no = int(input("Enter roll number: "))
marks = int(input("Enter marks (0-100): "))

# Validate marks and calculate grade
if marks < 0 or marks > 100:
    print("\nInvalid marks! Please enter a value between 0 and 100.")

else:
    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    elif marks >= 60:
        grade = "D"
    elif marks >= 50:
        grade = "E"
    else:
        grade = "F"

    print("\n===== STUDENT RESULT =====")
    print("Name  :", name)
    print("Roll No:", roll_no)
    print("Marks :", marks)
    print("Grade :", grade)

print("\n===== THANK YOU =====")
