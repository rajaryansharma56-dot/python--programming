
print("======================================")
print("       DIGITAL FOOTPRINT ANALYZER")
print("======================================")

name = input("Enter your name: ")

accounts = int(input("Enter total online accounts: "))
passwords = int(input("Accounts using same password: "))
profiles = int(input("Number of public profiles: "))
links = int(input("Unknown links clicked recently: "))
permissions = int(input("Apps with unnecessary permissions: "))

score = 0

score = score + (passwords * 10)
score = score + (profiles * 5)
score = score + (links * 15)
score = score + (permissions * 8)

print("\n======================================")
print("             RISK REPORT")
print("======================================")

print("User Name:", name)
print("Total Accounts:", accounts)
print("Risk Score:", score)

if score <= 20:
    print("Risk Level: LOW RISK")

elif score <= 50:
    print("Risk Level: MODERATE RISK")

elif score <= 80:
    print("Risk Level: HIGH RISK")

else:
    print("Risk Level: CRITICAL RISK")

print("\n------ SECURITY RECOMMENDATIONS ------")

if passwords > 0:
    print("Change reused passwords immediately.")

if profiles > 0:
    print("Review your public profile visibility.")

if links > 0:
    print("Avoid clicking unknown website links.")

if permissions > 0:
    print("Remove unnecessary app permissions.")

if score <= 20:
    print("Your digital security habits look good.")

print("\n======================================")
print("          ANALYSIS COMPLETED")
print("======================================")
