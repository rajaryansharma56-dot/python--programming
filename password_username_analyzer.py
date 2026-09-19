print("\n==== PASSWORD AND USERNAME SECURITY ANALYZER ====")

n = int(input("enter number of users : "))

strong_password_count = 0
weak_password_count = 0
valid_username_count = 0
invalid_username_count = 0
total_uppercase = 0
total_digits = 0

longest_password = None
longest_length = 0

for i in range(n):

    username = input("enter username : ")
    password = input("enter password : ")

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    uppercase_count = 0
    digit_count = 0

    for character in password:

        if character.isupper():
            has_upper = True
            uppercase_count += 1
            total_uppercase += 1

        elif character.islower():
            has_lower = True

        elif character.isdigit():
            has_digit = True
            digit_count += 1
            total_digits += 1

        elif character in "!@#$%&*":
            has_special = True

    if len(username) >= 5 and username.isalnum() and " " not in username:
        valid_username_count += 1
        username_valid = True
    else:
        invalid_username_count += 1
        username_valid = False

    if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
        strong_password_count += 1
        password_strong = True
    else:
        weak_password_count += 1
        password_strong = False

    if username_valid and password_strong:
        print(f"{username} : VALID ACCOUNT")
    else:
        print(f"{username} : INVALID ACCOUNT")

    if longest_password is None or len(password) > longest_length:
        longest_password = password
        longest_length = len(password)

print("\n==== ACCOUNT ANALYSIS ====")

print(f"strong passwords : {strong_password_count}")
print(f"weak passwords : {weak_password_count}")
print(f"valid usernames : {valid_username_count}")
print(f"invalid usernames : {invalid_username_count}")
print(f"longest password : {longest_password}")
print(f"longest password length : {longest_length}")
print(f"total uppercase letters : {total_uppercase}")
print(f"total digits : {total_digits}")

print("\n==== THANK YOU ====")
