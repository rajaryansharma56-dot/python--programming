# ==== STUDENT REPORT CARD =====

total_marks=0

highest_marks=None
lowest_marks=None

marks_90_count=0
marks_75_count=0

marks_50_count=0

failed_count=0


for i in range(1,11):
    n=int(input(f"enter number {i} :"))

    
    total_marks+=n 

    if n>=90:
        marks_90_count+=1

    elif n>=75:
        marks_75_count+=1
    elif n>=50:
        marks_50_count+=1
       
        
    else:
        
        failed_count+=1

    if highest_marks is None or n>highest_marks:
        highest_marks=n

    if lowest_marks is None or n<lowest_marks:
        lowest_marks=n

       
average_marks=total_marks/10

print("\n--- Student Marks Analysis ---")

print("Total marks:", total_marks)
print("Average marks:", average_marks)
print("Highest marks:", highest_marks)
print("Lowest marks:", lowest_marks)

print("\nNumber of students scoring 90 or above:", marks_90_count)
print("Number of students scoring 75 or above:", marks_75_count)
print("Number of students scoring 50 or above:",marks_50_count)
print("Number of students who failed:", failed_count)

print("\n ==== THANK YOU ====")
