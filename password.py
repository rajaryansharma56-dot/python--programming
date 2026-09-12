# ===== PASSWORD STRENGTH CHECKER =====

password = input("Enter your password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for char in password:

    if char.isupper():
        has_upper = True

    elif char.islower():
        has_lower = True

    elif char.isdigit():
        has_digit = True

    else:
        has_special = True


length_check = len(password) >= 8

print("\n===== PASSWORD STRENGTH CHECKER =====")

print("Length:", "✓" if length_check else "✗")
print("Uppercase:", "✓" if has_upper else "✗")
print("Lowercase:", "✓" if has_lower else "✗")
print("Digit:", "✓" if has_digit else "✗")
print("Special character:", "✓" if has_special else "✗")


conditions = 0

if length_check:
    conditions += 1

if has_upper:
    conditions += 1

if has_lower:
    conditions += 1

if has_digit:
    conditions += 1

if has_special:
    conditions += 1


if conditions == 5:
    print("\nPassword strength: STRONG")

elif conditions >= 3:
    print("\nPassword strength: MEDIUM")

else:
    print("\nPassword strength: WEAK")
