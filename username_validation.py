def check_username(username):
    if len(username)<6 or len(username)>12:
        return False

    if not username[0].isalpha():
        return False

    if " " in username:
        return False

    if not any(ch.isdigit() for ch in username):
        return False

    return True


username=input("enter username:")

if check_username(username):
    print("valid username")

else:
    print("invalid input ")
