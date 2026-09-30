print("\n ==== PASSWORD STRENGTH CHECKER ====  ")

password=input("enter your password : ")

length=len(password)

print("password length :",length)

if length<6:
    print("password strength : WEAK")

elif length<10:
    print("password strength : MEDIUM")

else:
    print("password strength : STRONG")


print("\n  ===== THANK YOU ===== ")
