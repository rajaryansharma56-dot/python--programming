print("\n ==== STUDENT ID VALIDATION ===== ")

student_id=input("enter  student id :")

if(len(student_id)==10 and student_id[0:3].isalpha() and student_id[0:3].isupper() and student_id[3:].isdigit() and " " not in student_id):
    print("VALID STUDENT ID ")

else:
    print("INVALID STUDENT ID ")

