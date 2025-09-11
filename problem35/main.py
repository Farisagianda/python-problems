"""

Problem: API Access Log Error Analysis

You are given:

    users.xlsx

user_id    department
101        HR
102        Engineering
103        Marketing
...

api_access.log — Each line is a JSON object, like:

    {"user_id": 101, "endpoint": "/login", "status_code": 500, "timestamp": "2025-07-29T14:25:30Z"}
    {"user_id": 102, "endpoint": "/get-data", "status_code": 200, "timestamp": "2025-07-29T15:00:10Z"}
    {"user_id": 101, "endpoint": "/submit-form", "status_code": 503, "timestamp": "2025-07-30T09:15:00Z"}
    {"user_id": 103, "endpoint": "/login", "status_code": 500, "timestamp": "2025-07-31T08:10:45Z"}

Your task:

Write a script that:

    Reads users.xlsx and creates a mapping of user_id → department.

    Reads api_access.log line-by-line (do not use f.read()).

    Filters:

        Requests within the last X days (--days CLI arg).

        Requests where status_code >= 500.

    Counts how many failed API calls happened per department.

    Saves results to failed_api_calls_by_department.csv:

    department,failed_count
    HR,5
    Engineering,12
    Marketing,3

Bonus:

    Handle the case where the same user exists in multiple departments (print a warning).

    Handle malformed JSON log lines gracefully.

    Print a summary to the console like:

    Total failed requests: 20
    Department with most failures: Engineering (12)
"""

import argparse
import datetime
import csv
import pandas
import json

def failedapi(excel, log, days):
    now = datetime.datetime.now(datetime.UTC)
    delta = datetime.timedelta(days=days)
    span = now - delta
    data = pandas.read_excel(excel)
    data = data.to_dict(orient="records")
    mapping = {}
    result = {}
    total = 0
    for record in data:
        user_id = record["user_id"]
        department = record["department"]
        if user_id in mapping and mapping[user_id] != department:
            print(f"Warning: User ID {user_id} already is assigned to department: {mapping.get(user_id)} (new: {department})")
        else:
            mapping[user_id] = department
    with open(log, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                line = json.loads(line)
            except json.JSONDecodeError:
                print(f"Skipping malformed JSON line: {line.strip()}")
                continue
            timestamp = line["timestamp"]
            time = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=datetime.UTC)
            if line["user_id"] in mapping and line["status_code"] >= 500 and time > span:
                userid = line["user_id"]
                result[mapping[userid]] = result.get(mapping[userid], 0) + 1
                total += 1
    print(f"Total failed request: {total}")
    if result:
        most_failed_dep = max(result, key=result.get)
        print(f"Department with most failures: {most_failed_dep} ({result[most_failed_dep]})")
    else:
        print("There are no failed API calls in all departments.")
    with open("failed_api_calls_by_department.csv", "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["department","failed_count"])
        for row in dict(sorted(result.items(), key=lambda x: x[1], reverse=True)):
            csvwriter.writerow([row, result[row]])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--days", type=int, required=True)
    args = parser.parse_args()
    failedapi("users.xlsx", "api_access.log", args.days)