"""
2. Parse CSV Log Files and Extract Errors
A log file is stored in CSV format:

timestamp,level,message
2025-03-29 14:30:15,INFO,Service started
2025-03-29 14:31:00,ERROR,Database connection failed
2025-03-29 14:32:45,WARNING,Memory usage high
2025-03-29 14:33:10,ERROR,Service crashed
Write a function that:

Reads the CSV input as a string.

Extracts only the rows where level is "ERROR".

Returns the extracted errors as a list of dictionaries.

Expected Output:

[
    {"timestamp": "2025-03-29 14:31:00", "message": "Database connection failed"},
    {"timestamp": "2025-03-29 14:33:10", "message": "Service crashed"}
]

"""
import csv
def main():
    ans = []
    with open("test.csv", "r") as csvfile:
        csvreader = csv.reader(csvfile)
        headers = next(csvreader)
        for row in csvreader:
            if 'ERROR' in row:
                d = {}
                d[headers[0]] = row[0]
                d[headers[2]] = row[2]
                ans.append(d)
    print(ans)
main()