print("\n student marks analyzer ")

n=int(input("enter number of students:"))

total_marks=0

passed=0
failed=0

for i in range(1,n+1):
    name=input(f"enter student name{i}:")
    roll_no=int(input(f"enter student roll number{i}:"))

    phy=float(input("enter physics marks"))
    chem=float(input("enter chemistry marks"))
    hindi=float(input("enter hindi marks"))
    bio=float(input("enter biology marks"))
    math=float(input("enter maths marks"))

    marks=phy+chem+hindi+bio+math

    total_marks=total_marks+marks

    average=total_marks/n

    if phy>=90:
     print("grade:A",phy)
    elif 80<=phy<=89:
     print("grade:B",phy)
    elif 70<=phy<=79:
     print("grade:C",phy)
    elif 60<=phy<=69:
     print("grade:D",phy)
    elif 50<=phy<=59:
     print("grade:E",phy)
    else:
     print("failed in physics")


    if chem>=90:
     print("grade:A",chem)
    elif 80<=chem<=89:
     print("grade:B",chem)
    elif 70<=chem<=79:
     print("grade:C",chem)
    elif 60<=chem<=69:
     print("grade:D",chem)
    elif 50<=chem<=59:
     print("grade:E",chem)
    else:
     print("failed in chemistry")


    if bio>=90:
     print("grade:A",bio)
    elif 80<=bio<=89:
     print("grade:B",bio)
    elif 70<=bio<=79:
     print("grade:C",bio)
    elif 60<=bio<=69:
     print("grade:D",bio)
    elif 50<=bio<=59:
     print("grade:E",bio)
    else:
     print("failed in biology")


    if math>=90:
     print("grade:A",math)
    elif 80<=math<=89:
      print("grade:B",math)
    elif 70<=math<=79:
     print("grade:C",math)
    elif 60<=math<=69:
     print("grade:D",math)
    elif 50<=math<=59:
     print("grade:E",math)
    else:
     print("FAILED IN MATHS")

    if hindi>=90:
     print("grade:A",hindi)
    elif 80<=hindi<=89:
     print("grade:B",hindi)
    elif 70<=hindi<=79:
     print("grade:C",hindi)
    elif 60<=hindi<=69:
     print("grade:D",hindi)
    elif 50<=hindi<=59:
     print("grade:E",hindi)
    else:
     print("failed in hindi")

    if phy>=40 and chem>=40 and math>=40 and hindi>=40 and bio>=40:
     print("passed")
     passed=passed+1

    else:
     print("failed")
     failed=failed+1

    average=marks/5


    print("\n ==== STUDENT REPORT CARD ====")
    print(f"student name {name}:")
    print(f"roll no {roll_no}:")
    print(f"total marks obtained {marks}:")
    print(f"number of students passed {passed}:")
    print(f"number of student failed {failed}:")
    print(f"average for the student {average},{name}:")

class_average=total_marks/n
print(f" class average {class_average}:")

print("\n ==== THNAK YOU ====  ")
