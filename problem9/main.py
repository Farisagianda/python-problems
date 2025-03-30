"""
Great! Here's a string modification question for you:

Problem: Transform a Log Message
You have a log message in the format:

"[ERROR] 2025-03-29 14:30:15 - Service failed to start"
Write a function that:

Extracts the log level (ERROR in this case).

Extracts the timestamp (2025-03-29 14:30:15).

Extracts the message (Service failed to start).

Returns a dictionary like this:

{
    "level": "ERROR",
    "timestamp": "2025-03-29 14:30:15",
    "message": "Service failed to start"
}
Would you like any constraints or extra challenges? 🚀
"""
def main(l):
    d = {}
    parts = l.split(' - ')
    d["message"] = parts[-1]
    level_timestamp = parts[0].split(' ')
    d["level"] = level_timestamp[0].strip('[]')
    d["timestamp"] = ' '.join(level_timestamp[1:])
    print(d)

l = "[ERROR] 2025-03-29 14:30:15 - Service failed to start"
main(l)