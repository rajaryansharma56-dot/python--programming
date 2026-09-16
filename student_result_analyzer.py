"\n student average marks calculator"

n=int(input("enter number of students :"))


student_passed_count=0
student_failed_count=0
record=[]

for i in range(n):
    name=input("enter student name :")
    math_marks=float(input("enter  math marks :"))
    phy_marks=float(input("enter physics marks "))

    average=(math_marks+phy_marks)/2
    record.append(average)



    if average>=75:
        print("excellent :")
        student_passed_count+=1
    elif average>=50:
        print("pass :")
        student_passed_count+=1
    else:
        print("fail :")
        student_failed_count+=1

    print("student name :",name)
    print("average marks :",average)
    print("RESULT :")

print("total number of students :",n)
print("number of students who passed :",student_passed_count)
print("number of students who failed :",student_failed_count)
print("students record :",record)
print("\n ==== THANK YOU ==== ")
