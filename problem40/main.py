"""
1) Easy — Extract username & IP from SSH auth.log
Input (sample):

Aug 12 10:31:02 ip-10-0-1-23 sshd[2142]: Failed password for alice from 203.0.113.9 port 50212 ssh2
Aug 12 10:31:07 ip-10-0-1-23 sshd[2142]: Accepted password for bob from 2001:db8:abcd::42 port 54422 ssh2
Aug 12 10:31:11 ip-10-0-1-23 sshd[2142]: Failed password for invalid user deploy-bot from 198.51.100.77 port 51515 ssh2

Task:
Write a script that reads from stdin or a file and prints CSV:

timestamp,username,ip,status

Extract username (handle “invalid user X”)
Extract ip (IPv4 and IPv6)
status ∈ {ACCEPTED, FAILED}

Edge cases: multiple spaces, usernames with hyphens/underscores, IPv6.

Follow-up: Add --since '2025-08-12 10:30:00' to only include recent lines.
"""
import argparse
import datetime
import csv
import re

class IPUsernameExtractor:
    def __init__(self):
        pass
    def ip_username_extractor(self, file, since):
        with open(file, "r") as f, \
        open("result.csv", "w", errors="replace") as csv_f:
            csvwriter = csv.writer(csv_f)
            csvwriter.writerow(["timestamp", "username", "ip", "status"])
            for line in f:
                line = line.strip()
                timestamp = re.search(r"(.*) ip.*", line).group(1)
                year = re.search(r"(\d+)", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")).group(1)
                timestamp = year + f" {timestamp}"
                time = datetime.datetime.strptime(timestamp, "%Y %b %d %H:%M:%S")
                if "invalid" not in line:
                    username = re.search(r".*for\s+(\S+)\s+", line).group(1)
                else:
                    username = re.search(r".*invalid\s+user\s+(\S+)\s+", line).group(1)
                ip = re.search(r".*from\s+(\S+)\s+", line).group(1)
                status = re.search(r":\s+(Failed|Accepted)\s+", line).group(1)
                if since and since <= time:
                    csvwriter.writerow([time, username, ip, status])
                elif not since:
                    csvwriter.writerow([time, username, ip, status])

DATA = "auth.log"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--since", type=datetime.datetime.fromisoformat, help="Put a timestamp like this 2025-08-12 10:30:00 to only include recent lines")
    args = parser.parse_args()
    ipusernameextractor = IPUsernameExtractor()
    ipusernameextractor.ip_username_extractor(DATA, args.since)
