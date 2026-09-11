text=input("enter a word or sentence :")

vowel_count=0

for ch in text:
    if ch.lower() in "aeiou":
        vowel_count+=1

print("number of vowels :", vowel_count)
