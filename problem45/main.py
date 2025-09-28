"""
Analyzes an application log file and extracts the top 5 most common ERROR messages.

Args:
    file_path (str): The path to the log file.

Behavior:
    - Use regex to capture log lines that start with "ERROR" or contain "ERROR <something>".
    - Group by error message (everything after the word "ERROR").
    - Return a list of tuples: (error_message, count), sorted in descending order.

Example log file:
[2025-09-27 10:00:01] INFO User login successful
[2025-09-27 10:00:02] ERROR Database connection failed
[2025-09-27 10:00:03] ERROR Timeout waiting for response
[2025-09-27 10:00:04] ERROR Database connection failed
[2025-09-27 10:00:05] INFO Task completed

Expected output:
[
    ('Database connection failed', 2),
    ('Timeout waiting for response', 1)
]
"""
import argparse
import re

def top_5_most_common_error_messages(logfile):
    error_counts = {}
    try:
        with open(logfile, "r") as f:
            data = f.read()
            if not data.strip():
                return "File is empty"
            errors = re.findall(r"\bERROR\s+(.*)", data)
            if not errors:
                return "There are no ERROR string in the file"
            for error in errors:
                if error_counts.get(error):
                    error_counts[error] += 1
                else:
                    error_counts[error] = 1
            return sorted(error_counts.items(), key=lambda x: x[1], reverse=True)[:5]
    except FileNotFoundError:
        print("Error. File not found.")
        return []
    except PermissionError:
        print("Error. File cannot be read.")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--logfile", default="access.log", type=str)
    args = parser.parse_args()
    print(top_5_most_common_error_messages(args.logfile))