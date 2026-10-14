print("\n === STUDENT RESULT ANALYZER ===  ")

python=int(input("enter python marks:"))

chemistry=int(input("enter chemistry marks:"))

math=int(input("enter maths marks :"))

category=""

average=(python+chemistry+math)/3

if python<35 or chemistry<35 or math<35:
    
    category="FAIL"

else:
    

    if average>=75:
     category="DISTINCTION"
    elif average>=50:
     category="PASS"
    
    else:
     category="SECOND CLASS"

print("average marks obtained",average)
print("result",category)
