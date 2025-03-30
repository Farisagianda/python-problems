"""
Problem: Normalize JSON Logs
You have a log in JSON format representing an event in a system. The log contains extra fields, but you only need to extract specific keys and rename them.

Example Input (JSON log as a string):
{
    "log_level": "INFO",
    "event_time": "2025-03-29T14:30:15Z",
    "user": {
        "id": 12345,
        "name": "john_doe"
    },
    "details": "User logged in successfully",
    "extra": {
        "ip": "192.168.1.1",
        "user_agent": "Mozilla/5.0"
    }
}
Your Task:
Extract and rename keys:

"log_level" → "level"

"event_time" → "timestamp"

"details" → "message"

"user.id" → "user_id"

Ignore unnecessary fields like "extra" and "user.name".

Return a dictionary in this format:

{
    "level": "INFO",
    "timestamp": "2025-03-29T14:30:15Z",
    "message": "User logged in successfully",
    "user_id": 12345
}
⚠ Constraints:

The input is a JSON string, so you must parse it first.

Do not use any external libraries (only built-in modules).

Ignore any missing fields (handle gracefully).
"""
def main():
    d = {}
    with open("test.log", "r") as f:
        lines = f.readlines()
    for l in lines:
        if "log_level" in l:
            l = l.strip().strip(',').replace('"', '')
            parts = l.split(": ")
            d["level"] = parts[-1]
        if "event_time" in l:
            l = l.strip().strip(',').replace('"', '')
            parts = l.split(": ")
            d["timestamp"] = parts[-1]
        if "details" in l:
            l = l.strip().strip(',').replace('"', '')
            parts = l.split(": ")
            d["message"] = parts[-1]
        if "user.id" in l:
            l = l.strip().strip(',').replace('"', '')
            parts = l.split(": ")
            d["user_id"] = parts[-1]
    print(d)

main()