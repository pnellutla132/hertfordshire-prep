try:
    with open("security_log.txt", "r") as file:
        logs = file.readlines()
high_cpu=0
high_memory=0
high_desk=0
critical_events=0

for line in logs:
    if "HIGH CPU USAGE" in line:
        high_cpu=+1
        critical_events.append(line)
    if "high memory usage" in line:
        high_memory=+1
        critical_events.append(line)
    if "high disk usage" in line:
        high_desk=+1
        critical_events.append(line)


print("summary report")
print(f"HIGH CPU USAGE: {high_cpu}")
print(f"HIGH MEMORY USAGE: {high_memory}")
print(f"HIGH DISK USAGE: {high_desk}")
print(f"CRITICAL EVENTS: {len(critical_events)}")

except FileNotFoundError:
    print("Error: system_monitor_log.txt not found!")
    print("Please run your Day 2 or Day 3 script first to generate the log file.")

except Exception as e:
    print(f"Unexpected error: {e}")
