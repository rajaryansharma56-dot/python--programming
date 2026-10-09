def recurring_char(text):
    for i in text:
        if text.count(i)>1:
            return i
    return "no recurring character"

text=input("enter a string:")

result=recurring_char(text)

print("recurring character",result)
