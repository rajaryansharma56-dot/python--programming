print("\n ==== USER NAME VALIDATION ==== ")

user_name=input("enter your name :")

has_digit=False

for ch in user_name:
    if ch.isdigit():
        has_digit=True
        break

if (6<=len(user_name)<=12 and user_name[0].isalpha() and has_digit and " " not in user_name):
    print("VALID USERNAME :")
else:
    print("INVALID USERNAME :")
