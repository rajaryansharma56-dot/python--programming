print("\n ==== LEADER SELECTION ====  ")

n=int(input("enter number of students :"))

highest_mark=None

topper=0

marks=[]

for i in range(n):
    mark=int(input(f"enter mark of student {i}:"))

    marks.append(mark)

    if highest_mark is None or mark>highest_mark:
        highest_mark=mark
        topper=i


    print("highest marks",highest_mark)
    print("topper",topper)
