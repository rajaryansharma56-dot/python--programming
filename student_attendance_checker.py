print("\n ===== STUDENT ATTENDANCE CHECKER ==== ")

name=input("enter student name :")
classes=int(input(" enter number of classes held :"))
classes_attend=int(input(" enter number of classes attended :"))

attendance=(classes_attend/classes)*100

if attendance>=75:
    print("Eligible for exam:",name)

else:
    print("Not Eligible for exam",name)

print("STUDENT NAME :",name)
print("ATTENDANCE :",attendance)

print("\n ===== THANK YOU ==== ")
