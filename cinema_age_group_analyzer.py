print("\n ==== CINEMA SEAT CHECKER ==== ")

n=int(input("enter number of customers : "))

child_count=0
tenn_count=0
adult_count=0
senior_count=0

for i in range(1,n+1):
    age=int(input(f"enter age of customer {i}:"))

    if age<0:
        print("invalid input:")

    else:
        if age<13:
            child_count=child_count+1

        elif 13<=age<=19:
            tenn_count=tenn_count+1

        elif 20<=age<=59:
            adult_count=adult_count+1

        else:
            senior_count=senior_count+1


print("\nChildren:",child_count)
print("Teenagers:",tenn_count)
print("Adults:",adult_count)
print("Senior citizens:",senior_count)


largest=child_count

if tenn_count>largest:
    largest=tenn_count

if adult_count>largest:
    largest=adult_count

if senior_count>largest:
    largest=senior_count


print("\nLargest group:")

if child_count==largest:
    print("Children")

if tenn_count==largest:
    print("Teenagers")

if adult_count==largest:
    print("Adults")

if senior_count==largest:
    print("Senior citizens")


print("\n ==== END OF THE CODE ==== ")
