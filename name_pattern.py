import re

username=input("enter your username :").strip()

pattern=r"[a-zA-Z][a-zA-Z0-9_]*"

if len(username)>=5 and len(username)<=15:
    if re.fullmatch(pattern,username):
        print("valid name:")
    else:
        print("invalid name :")
else:
    print("invalid name :")
