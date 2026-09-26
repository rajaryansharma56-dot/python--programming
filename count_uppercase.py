text=input("enter a string :")

count=0

for char in text:
    if char.isupper():
        count+=1

print("number of uppercase letter :",count)
