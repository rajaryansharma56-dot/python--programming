print("\n ==== STUDENT ANALYZER ====  ")

n=int(input("enter number of students :"))

highest_mark=None
lowest_mark=None

student_passed=0
student_failed=0
total_mark=0
no_above=0

mark_list=[]

for i in range(1,n+1):
    marks=int(input(f"enter marks of student {i}:"))
    
    mark_list.append(marks)
    total_mark=total_mark+marks



    if marks<0 or marks>100:
        print("invalid input")



    elif marks>=40:
        student_passed=student_passed+1

    else:

        student_failed=student_failed+ 1
      

    if highest_mark is None or marks>highest_mark:
        highest_mark=marks

    if lowest_mark is None or marks<lowest_mark:
        lowest_mark=marks

average=total_mark/n

for marks in mark_list:


    if marks>average:
        no_above=no_above+ 1

print("\n ==== STUDENT ANALYZER ==== ")
print("HIGHEST MARK :",highest_mark)
print("LOWEST MARK :",lowest_mark)
print("CLASS AVERAGE :",average)
print("NUMBER OF STUDENTS PASSED :",student_passed)
print("NUMBER OF STUDENTS FAILED :",student_failed)
print("NUMBER OF STUDENTS ABOVE AVERAGE :",no_above)
print("===== THANK YOU =====")
