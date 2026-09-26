text=input("enter a string :")

count=0

for char in text:
    if char.islower():
        count+=1


print("number of lower case in letters in string is :",count)
