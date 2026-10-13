print("\n === STUDENT PERFORMANCE ANALYZER === ")

n=int(input("enter number of students: "))

highest_marks=None
lowest_marks=None

distinction=0
first_class=0
passed=0
failed=0

above_class_avg=0
total=0
class_marks=[]

for i in range(1,n+1):

    marks=int(input(f"enter marks {i}: "))

    while marks<0 or marks>100:
        print("INVALID INPUT")
        marks=int(input(f"enter valid marks for student {i}: "))

    class_marks.append(marks)
    total=total+marks

    if marks>=75:
        print("Category: Distinction",marks)
        distinction=distinction+1

    elif marks>=60:
        print("Category: First Class",marks)
        first_class=first_class+1

    elif marks>=40:
        print("Category: Pass",marks)
        passed=passed+1

    else:
        print("Category: Fail",marks)
        failed=failed+1

    if highest_marks is None or marks>highest_marks:
        highest_marks=marks

    if lowest_marks is None or marks<lowest_marks:
        lowest_marks=marks
        


average=total/n

for marks in class_marks:

    if marks>average:
        above_class_avg=above_class_avg+1

print("\n === CLASS PERFORMANCE === ")



print(f"total marks of the entire class: {total}")
print(f"average marks of the entire class: {average:.2f}")
print(f"highest marks in the class: {highest_marks}")
print(f"lowest marks in the class: {lowest_marks}")



print(f"number of distinction students: {distinction}")
print(f"number of first class students: {first_class}")
print(f"number of passed students: {passed}")
print(f"number of failed students: {failed}")
print(f"students scoring above class average: {above_class_avg}")

print("\n === THANK YOU ===")
