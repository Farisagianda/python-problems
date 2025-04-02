"""
5. Extract Process Info from ps aux Output
A system administrator runs ps aux and gets this output:

USER       PID %CPU %MEM COMMAND
root      1234  12.5  5.2 nginx
user1     5678   2.1  1.0 python3 script.py
user2     9101   0.5  0.3 bash
Write a function that:

Extracts PID, %CPU, and COMMAND.

Returns a list of processes, sorted by %CPU in descending order.

Expected Output:
[
    {"pid": 1234, "cpu": 12.5, "command": "nginx"},
    {"pid": 5678, "cpu": 2.1, "command": "python3 script.py"},
    {"pid": 9101, "cpu": 0.5, "command": "bash"}
]
"""
def main(n):
    ans = []
    line = [k.split(None, 4) for k in n.strip().split("\n")]
    header = line[0]
    content = line[1:]
    for part in content:
        d = {}
        for i,v in enumerate(header):
            if v.lower() == "pid" or v == "%CPU":
                d[v.lower().strip('%')] = float(part[i])
            elif v.lower() == "command":
                d[v.lower()] = part[i]
        ans.append(d)
    ans = sorted(ans, key=lambda x: x['cpu'], reverse=True)
    print(ans)

n = """
USER       PID %CPU %MEM COMMAND
root      1234  12.5  5.2 nginx
user1     5678   2.1  1.0 python3 script.py
user2     9101   0.5  0.3 bash"""

main(n)
