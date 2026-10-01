print("\n ==== WORD AND CHARACTER COUNT ====\n")

sentence=input("enter a sentence :")

words=sentence.split()

total_words=len(words)
characters=0
vowel_words=0
consonant_words=0

for word in words:
    characters+=len(word)

    if word[0] in "aeiouAEIOU":
        vowel_words+=1

    elif word[0].isalpha():
        consonant_words+=1

print("\nTotal words:", total_words)
print("Characters excluding spaces:", characters)
print("Words starting with vowel:", vowel_words)
print("Words starting with consonant:", consonant_words)

print("\n==== THANK YOU ====")
