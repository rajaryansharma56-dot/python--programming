print("\n ==== EVENT COUNTER ====   ")

string=input("enter your text")

uppercase=0
lowercase=0
digit=0
special=0

for ch in string:
    if ch.isupper():
        uppercase=uppercase+1

    elif ch.islower():
        lowercase=lowercase+1
    elif ch.isdigit():
        digit=digit+1

    else:
        special=special+1

maximum=max(uppercase,lowercase,digit,special)

if uppercase==maximum:
    print("UPPERCASE HAS HIGHEST COUNT ")

if lowercase==maximum:
    print("LOWERCASE HAS HIGHEST COUNT ")

if digit==maximum:
    print("DIGIT HAS HIGHEST COUNT ")

if special==maximum:
    print("SPECIAL HAS HIGHEST COUNT ")event_counter.py
