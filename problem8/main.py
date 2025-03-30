"""8. Parse & Extract Fields from JSON Logs
Problem:
Given a JSON-based log file, extract all unique error messages.

Example Input:

logs = [
    {"timestamp": "2024-03-29T12:00:00Z", "level": "INFO", "message": "Service started"},
    {"timestamp": "2024-03-29T12:01:00Z", "level": "ERROR", "message": "Database connection failed"},
    {"timestamp": "2024-03-29T12:02:00Z", "level": "ERROR", "message": "Timeout on API request"},
    {"timestamp": "2024-03-29T12:03:00Z", "level": "ERROR", "message": "Database connection failed"},
]

Expected Output:

["Database connection failed", "Timeout on API request"]"""
2
def main():
    d = {}
    s = set()
    with open("test.log", "r") as f:
        for line in f:
            line = line.replace('"', '').replace('{', '').replace('}', '')
            lines = line.split(', ')
            for i in lines:
                k,v = i.split(":", 1)
                d[k] = v.strip().strip(',')
            if d["level"] == "ERROR":
                s.add(d["message"])
    print(list(s))

main()