print("\n ==== USERNAME VALIDATION PROGRAM ==== ")

username=input("enter user name :")

has_upper=False
has_digit=False


for ch in username:
    if ch.isupper():
        has_upper=True
    if ch.isdigit():
        has_digit=True

if(8<=len(username)<=15 and username[0].isalpha() and has_upper and has_digit and "@" not in username and "#" not in username):
    print("VALID USERNAME ")

else:
    print("INVALID USERNAME")

print("thank you")
