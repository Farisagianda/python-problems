"""
1. Log Parsing & Alerting
Write a Python script that:

Reads a log file (app.log) line-by-line without loading the whole file into memory.

Detects if any line contains "ERROR" and "Database" within the same line.

Prints the matching line and writes it to an alerts.log file.

Keeps running and watching the file for new logs (like tail -f).

Follow-up: Make it configurable so the keywords can be passed as command-line arguments.

"""
import argparse
import time
import sys

class LogTransformer:
    def __init__(self):
        pass
    def log_parser(self, file, keywords, streaming=False, include_history=True):
        try:
            with open("alerts.log", 'a', encoding="utf-8") as alert_f, \
            open(file, 'r', encoding="utf-8", errors="replace") as f:
                print("Alerted log lines:")
                if not streaming or include_history:
                    for line in f:
                        line = line.strip()
                        if not line:
                            continue
                        if all(x in line for x in keywords):
                            print(f"  {line}")
                            alert_f.write(line + "\n")
                            alert_f.flush()
                if streaming:
                    if not include_history:
                        f.seek(0, 2)
                    while True:
                        line = f.readline()
                        if not line:
                            time.sleep(0.5)
                            continue
                        line = line.strip()
                        if all(x in line for x in keywords):
                            print(line)
                            alert_f.write(line + "\n")
                            alert_f.flush()
        except KeyboardInterrupt:
            print("\nStopped.", file=sys.stderr)
        except FileNotFoundError:
            print(f"\nFile not found: {file}", file=sys.stderr)
            sys.exit(1)


DATA = "app.log"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    parser.add_argument("--keywords", required=False, nargs="+", default=["ERROR", "Database"])
    parser.add_argument("--streaming", required=False, action="store_true")
    parser.add_argument("--no-history", required=False, action="store_true")
    args = parser.parse_args()
    log_transformer = LogTransformer()
    log_transformer.log_parser(
        args.file,
        args.keywords,
        args.streaming,
        not args.no_history
    )