
print("========================================")
print("          API SENTINEL")
print("       BACKEND LOG ANALYZER")
print("========================================")

logs = [
    "192.168.1.10,LOGIN,200,120",
    "192.168.1.11,LOGIN,401,90",
    "192.168.1.11,LOGIN,401,100",
    "192.168.1.11,LOGIN,401,110",
    "192.168.1.12,GET_USERS,200,250",
    "192.168.1.13,GET_DATA,500,180",
    "192.168.1.14,UPLOAD,503,220",
    "192.168.1.10,GET_USERS,200,150",
    "192.168.1.15,SEARCH,200,1800",
    "192.168.1.16,LOGIN,403,100"
]

total = 0
success = 0
failed = 0
errors = 0
slow = 0
total_time = 0
failed_login = 0

print("\nANALYZING SERVER LOGS...")
print("----------------------------------------")

for log in logs:

    data = log.split(",")

    ip = data[0]
    endpoint = data[1]
    status = int(data[2])
    response = int(data[3])

    total = total + 1
    total_time = total_time + response

    if status >= 200 and status < 300:
        success = success + 1

    elif status >= 400:
        failed = failed + 1

    if status >= 500:
        errors = errors + 1

    if response > 1000:
        slow = slow + 1

    if endpoint == "LOGIN" and status == 401:
        failed_login = failed_login + 1

    print("\nIP:", ip)
    print("Endpoint:", endpoint)
    print("Status:", status)
    print("Response:", response, "ms")

# CALCULATIONS

average = total_time / total
success_rate = (success / total) * 100
failure_rate = (failed / total) * 100

# FINAL REPORT

print("\n========================================")
print("           SERVER REPORT")
print("========================================")

print("Total Requests:", total)
print("Successful Requests:", success)
print("Failed Requests:", failed)
print("Server Errors:", errors)
print("Slow Requests:", slow)
print("Failed Login Attempts:", failed_login)

print("Average Response Time:", round(average, 2), "ms")
print("Success Rate:", round(success_rate, 2), "%")
print("Failure Rate:", round(failure_rate, 2), "%")

# SECURITY STATUS

print("\n========================================")
print("           SECURITY STATUS")
print("========================================")

if failed_login >= 3:
    print("WARNING: Suspicious login activity detected!")

else:
    print("No suspicious login activity.")

# SERVER STATUS

print("\n========================================")
print("            SYSTEM STATUS")
print("========================================")

if errors >= 3 or failure_rate >= 50:
    print("STATUS: CRITICAL")

elif errors > 0 or slow > 0:
    print("STATUS: WARNING")

else:
    print("STATUS: HEALTHY")

# SAVE REPORT

file = open("sentinel_report.txt", "w")

file.write("API SENTINEL REPORT\n")
file.write("-------------------\n")
file.write("Total Requests: " + str(total) + "\n")
file.write("Successful Requests: " + str(success) + "\n")
file.write("Failed Requests: " + str(failed) + "\n")
file.write("Server Errors: " + str(errors) + "\n")
file.write("Slow Requests: " + str(slow) + "\n")
file.write("Average Response Time: " + str(round(average, 2)) + " ms\n")

file.close()

print("\nReport saved successfully!")
print("========================================")
vapi_sentinel.py
