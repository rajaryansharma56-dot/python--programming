print("\n ==== EMAIL VALIDATION ==== ")

email=input("enter email :")

if (email.count("@")==1 and "." in email[email.index("@")] and "" not in email and email.startswith(("@","."))):
    print("VALID EMAIL")

else:
    print("INVALID EMAIL ")

print("\n ==== THNAK YOU ==== ")
