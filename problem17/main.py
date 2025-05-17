"""
1. Parse Logs and Extract Error Rates

You are given a log file with lines like:

2024-05-16 13:04:05 [INFO] Request succeeded
2024-05-16 13:04:06 [ERROR] Timeout while contacting db

Task: Calculate the percentage of log entries that are errors.
"""

def main():
    count = 0
    total = 0
    with open("test.log", "r") as f:
        data = f.readlines()
    for line in data:
        line = line.strip()
        if not line:
            continue
        total += 1
        if "[ERROR]" in line.upper():
            count += 1
    if total == 0:
        print("Log file is empty")
    error_rate = count/total * 100
    print(f"Error percentage rate in the log file: {error_rate:.2f}%")

if __name__ == "__main__":
    main()