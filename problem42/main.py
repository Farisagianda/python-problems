'''
## Problem: Parse `ps aux` Output and Find Top Memory Consumers

A system administrator runs `ps aux` and gets this sample output:

```
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.1 225272  1100 ?        Ss   Sep10   0:04 /sbin/init
daemon     231  0.0  1.2  45000 12500 ?        Ss   Sep10   0:20 /usr/sbin/daemon
postgres   890  1.2 15.4 800000 160000 ?       Sl   Sep10  20:15 postgres: writer
nginx     1203  0.5  5.3 300000 55000 ?        S    Sep10   2:45 nginx: worker
```

### Task

Write a function that:

1. Parses this output.
2. Extracts **USER**, **PID**, **%CPU**, **%MEM**, and **COMMAND**.
3. Returns the **top N processes by %MEM usage** (descending order).
4. The result should be a list of dictionaries.

### Example Call

```python
print(top_memory_processes(ps_output, 2))
```

### Expected Output

```python
[
    {"user": "postgres", "pid": 890, "cpu": 1.2, "mem": 15.4, "command": "postgres: writer"},
    {"user": "nginx", "pid": 1203, "cpu": 0.5, "mem": 5.3, "command": "nginx: worker"}
]
```
'''
class Parser:
    def __init__(self):
        pass

    def top_memory_processes(self, data, n):
        ans = []
        lines = data.strip().splitlines()
        for line in lines[1:]:
            groups = line.split(maxsplit=10)
            ans.append({"user": groups[0], "pid":  int(groups[1]), "cpu": float(groups[2]), "mem": float(groups[3]), "command": groups[10].strip()})
        ans = sorted(ans, key=lambda x: float(x["mem"]), reverse=True)
        print(ans[:n])
        return ans[:n]




ps_output = '''
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.1 225272  1100 ?        Ss   Sep10   0:04 /sbin/init
daemon     231  0.0  1.2  45000 12500 ?        Ss   Sep10   0:20 /usr/sbin/daemon
postgres   890  1.2 15.4 800000 160000 ?       Sl   Sep10  20:15 postgres: writer
nginx     1203  0.5  5.3 300000 55000 ?        S    Sep10   2:45 nginx: worker
'''

parser = Parser()
parser.top_memory_processes(ps_output, 2)