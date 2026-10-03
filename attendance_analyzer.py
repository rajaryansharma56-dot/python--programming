print("\n ==== ATTENDANCE ANALYZER ==== ")

present=0
absent=0

for i in range(1,8):
    status=input(f"enter attendance for day{i} (P/A) :")

    if status=="P" or status=="p":
        present+=1

    elif status=="A" or status=="a":
        absent+=1

attendance=(present/7)*100

if attendance>=90:
    category="EXCELLENT ATTENDANCE"

elif attendance>=75:
    category="GOOD ATTENDANCE"

else:
    category="LOW ATTENDANCE"

if attendance>=75:
    eligibility="ELIGIBLE"
else:
    eligibility="NOT ELIGIBLE"

print("\n ==== ATTENDANCE RESULT ====")
print("present days :",present)
print("absent days :",absent)
print("attendance :",attendance,"%")
print("category :",category)
print("eligibility :",eligibility)

print("\n ==== THANK YOU ====")
