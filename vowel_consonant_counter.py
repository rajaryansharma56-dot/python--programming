print("\n ==== VOWEL COUNTER ====  ")

sentence=input("enter a sentence :")

vowels=0

consonants=0

for ch in sentence:
    if ch in"aeiouAEIOU":
        vowels+=1
    elif ch.isalpha():
        consonants+=1

print("vowels:",vowels)
print("consonants:",consonants)

print("\n ==== THANK YOU ==== ")
