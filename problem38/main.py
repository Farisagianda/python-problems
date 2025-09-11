"""
Multi-file Tail & Burst Detector
Goal
Watch multiple log files in real time, filter lines, and raise an alert when errors burst above a threshold in a rolling time window.

Inputs
You’ll get two logs (example fixtures below):

    api-a.log

    2025-08-10T19:26:00Z INFO  Startup complete
    2025-08-10T19:26:10Z ERROR Database timeout req_id=abc123
    2025-08-10T19:26:20Z WARN  Slow query 4200ms
    2025-08-10T19:26:25Z ERROR Payment gateway failed req_id=def456
    2025-08-10T19:27:05Z ERROR Database timeout req_id=xyz999

    api-b.log

    2025-08-10T19:26:02Z INFO  Ready
    2025-08-10T19:26:11Z ERROR Cache miss storm shard=4
    2025-08-10T19:26:12Z ERROR Cache backend down shard=4
    2025-08-10T19:27:10Z INFO  Recovered

Requirements
1. Streaming tail

  Watch multiple files given by --files (space-separated list or glob).

  If --include-history is not set, start from EOF (like tail -f).

2. Filtering

  Include lines that match all --include keywords (default: ERROR).

  Exclude lines that contain any of --exclude keywords (optional).

  --ignore-case flag to do case-insensitive matching.

3. Burst detection (rolling window)

    Maintain a rolling window of the last --window-sec seconds (default: 60).

    Per file, if matched line count in the window ≥ --threshold (default: 3), emit an ALERT to stdout:

        ALERT file=api-a.log count=3 window=60s at=2025-08-10T19:27:05Z

    Add a --cooldown-sec (default: 60) to avoid spamming repeated alerts for the same file.

4. Output

    Write each matched line to alerts.csv as:

    timestamp,file,level,message
    (Extract level from the token after the timestamp, e.g., ERROR/WARN/INFO.)

5. Rotation handling

    If a file shrinks (size decreases) or disappears/reappears, automatically reopen and continue (simulate logrotate copytruncate).

6. Graceful shutdown

    On CTRL+C, print a final summary:

        Summary: api-a.log=3, api-b.log=2 (window=60s)

7. CLI

    python burst_detector.py \
      --files api-a.log api-b.log \
      --include ERROR Database \
      --exclude timeout \
      --ignore-case \
      --window-sec 60 \
      --threshold 3 \
      --cooldown-sec 60 \
      --include-history


8. Bonus (optional)
    --json to also append JSON Lines to alerts.jsonl with fields: {timestamp, file, level, message}.

    --any to match if any include keyword is present (instead of all).

    Prometheus-style /metrics on --port exposing per-file match counts.

"""

import argparse
import csv
import re

class BurstDetector:
    def __init__(self):
        pass

    def multifile_burst_detector(self, files, include, exclude, ignore_case, window_sec, threshold, cooldown, include_history):
        result_file = "alerts.csv"
        for file in files:
            with open(file, "r", encoding="utf-8", errors="replace") as f, \
            open(result_file, "a", encoding="utf-8") as result_f:
                if not include_history:
                    f.seek(0, 2)
                for line in f:
                    line = line.strip()
                    #print(line)
                    groups = re.search(r'(\S+Z)\s+(INFO|WARN|ERROR)\s+(.*)', line)
                    timestamp = groups.group(1)
                    level = groups.group(2)
                    message = groups.group(3)
                    for word in include:
                        csvwriter = csv.writer(result_f)
                        csvwriter.writerow(["timestamp", "file", "level", "message"])
                        if word in line:
                            csvwriter.writerow(word)




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", nargs="+", required=True)
    parser.add_argument("--include", nargs="+", required=True)
    parser.add_argument("--exclude", nargs="+")
    parser.add_argument("--ignore-case", action="store_true")
    parser.add_argument("--window-sec", type=int, default=60)
    parser.add_argument("--threshold", type=int, default=3)
    parser.add_argument("--cooldown", type=int, default=60)
    parser.add_argument("--include-history", action="store_true")
    args = parser.parse_args()
    burstdetector = BurstDetector()
    burstdetector.multifile_burst_detector(
        args.files,
        args.include,
        args.exclude,
        args.ignore_case,
        args.window_sec,
        args.threshold,
        args.cooldown,
        args.include_history
    )