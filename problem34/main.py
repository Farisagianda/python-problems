"""
Problem Statement
You are a production engineer in charge of monitoring a payment processing service.
The system generates daily log files in JSON Lines format (.log), where each line is a JSON object with the following structure:

{
  "timestamp": "2025-08-01T14:23:05Z",
  "transaction_id": "TX123456",
  "status": "FAILED",
  "error_code": "INSUFFICIENT_FUNDS",
  "amount": 49.99,
  "currency": "USD",
  "user_id": 9876
}
Separately, your finance team keeps an Excel file (users.xlsx) with user details:

user_id	account_type	region
9876	premium	US
1234	free	UK
...	...	...

Task
Write a Python script to:

    Load the Excel file and store user info in a lookup table.

    Read the JSON log file line by line (it could be large — don’t load all into memory at once).

    Filter log entries to only include ones that:

        Occurred in the last 24 hours from the current time

        Have "status": "FAILED"

    Join with user data from the Excel file so that each log entry contains account_type and region.

    Count the number of failed transactions per region in the last 24 hours.

    Save the results into a CSV file (failed_transactions_by_region.csv) with columns:

    region,failed_count
    US,10
    UK,5
    ...


    Example Input
    Excel (users.xlsx):

    user_id	account_type	region
    9876	premium	US
    1234	free	UK

    Logs (transactions.log):


    {"timestamp": "2025-08-01T14:23:05Z", "transaction_id": "TX123456", "status": "FAILED", "error_code": "INSUFFICIENT_FUNDS", "amount": 49.99, "currency": "USD", "user_id": 9876}
    {"timestamp": "2025-08-01T10:15:12Z", "transaction_id": "TX789101", "status": "SUCCESS", "error_code": null, "amount": 10.00, "currency": "USD", "user_id": 1234}
    {"timestamp": "2025-08-01T15:30:45Z", "transaction_id": "TX543210", "status": "FAILED", "error_code": "CARD_EXPIRED", "amount": 15.00, "currency": "GBP", "user_id": 1234}



    Hints
    Use datetime.datetime.utcnow() with timedelta(days=1) to filter logs.

    Use pandas.read_excel() for reading the Excel file.

    Use json.loads() for parsing each log line.

    Use csv module or pandas to write results.
"""

import datetime
import pandas as pd
import json
import csv
import argparse

def read_excel(file, log, days):
    raw_data = pd.read_excel(file)
    data = raw_data.to_dict(orient="records")
    user_region = {}
    result = {}
    for record in data:
        user_id = record["user_id"]
        region = record["region"]
        if user_id in user_region and user_region[user_id] != region:
            print(f"WARNING: User ID already has a region {user_region.get(user_id)} assigned to it")
        else:
            user_region[user_id] = region
    with open(log, "r") as f:
        now = datetime.datetime.now(datetime.UTC)
        delta = datetime.timedelta(days=days)
        span = now - delta
        for line in f:
            line = line.strip()
            if not line:
                continue
            json_obj = json.loads(line)
            userid = json_obj["user_id"]
            timestamp = json_obj["timestamp"]
            timestamp = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=datetime.UTC)
            if userid in user_region and timestamp > span and json_obj["status"] == "FAILED":
                result[user_region[userid]] = result.get(user_region[userid], 0) + 1
    with open("failed_transactions_by_region.csv", "w", newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["region", "failed_count"])
        for region in sorted(result):
            csvwriter.writerow([region, result[region]])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--days", required=True, type=int, help="Past x number of days to check from log file.")
    args = parser.parse_args()
    read_excel("users.xlsx", "transactions.log", args.days)

"""
Follow‑up:
Right now your script always counts failed transactions in the last 2 days.
How would you modify your program so the time window is configurable via a command‑line argument, e.g. --days 7 to get the last 7 days instead of 2?

Bonus: How would you handle the case where the Excel file might contain duplicate user_id entries with different regions?
"""