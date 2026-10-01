print("\n ===== string analyze =====")

string=input("enter a string :")

uppercase_count=0
lowercase_count=0
digit_count=0
spaces_count=0
special_count=0


for char in string:
    if char.isupper():
        uppercase_count+=1
    elif char.islower():
        lowercase_count+=1
    elif char.isdigit():
        digit_count+=1
    elif char==" ":
        spaces_count+=1
    else:
        special_count+=1


print("upper case letters :",uppercase_count)
print("lower case letters :",lowercase_count)
print("digits :",digit_count)
print("spaces :",spaces_count)
print("special characters :",special_count)

print("\n ==== THANK YOU ====")
