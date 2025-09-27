'''
Here’s a tougher one that’s super practical for ops folks like you:

## Problem: Parse Nginx Access Logs and Report Slow Endpoints

You’re given Nginx access logs in this (common) format:

```
$remote_addr - $remote_user [$time_local] "$request" $status $body_bytes_sent $request_time "$http_referer" "$http_user_agent"
```

### Sample Input

```
10.0.0.1 - - [12/Sep/2025:18:50:01 +0000] "GET /api/users?id=1 HTTP/1.1" 200 123 0.120 "-" "curl/8.0"
10.0.0.2 - - [12/Sep/2025:18:50:02 +0000] "GET /api/users?id=2 HTTP/1.1" 200 150 0.240 "-" "curl/8.0"
10.0.0.3 - - [12/Sep/2025:18:50:03 +0000] "GET /api/users?id=3 HTTP/1.1" 500 50 0.300 "-" "curl/8.0"
10.0.0.4 - - [12/Sep/2025:18:50:04 +0000] "POST /api/login HTTP/1.1" 401 20 0.050 "-" "curl/8.0"
10.0.0.5 - - [12/Sep/2025:18:50:05 +0000] "POST /api/login HTTP/1.1" 200 20 0.070 "-" "curl/8.0"
10.0.0.6 - - [12/Sep/2025:18:50:06 +0000] "GET /static/app.js HTTP/1.1" 200 2048 0.005 "-" "curl/8.0"
10.0.0.7 - - [12/Sep/2025:18:50:07 +0000] "GET /api/users?id=4 HTTP/1.1" 200 120 0.180 "-" "curl/8.0"
10.0.0.8 - - [12/Sep/2025:18:50:08 +0000] "GET /api/users?id=5 HTTP/1.1" 200 110 0.090 "-" "curl/8.0"
10.0.0.9 - - [12/Sep/2025:18:50:09 +0000] "GET /favicon.ico HTTP/1.1" 200 300 0.002 "-" "curl/8.0"
10.0.0.10 - - [12/Sep/2025:18:50:10 +0000] "POST /api/login HTTP/1.1" 500 20 0.400 "-" "curl/8.0"
```

### Task

Write a function `top_slow_endpoints(log_text: str, n: int) -> list[dict]` that:

1. Parses each line.
2. Normalizes the request **path** by removing the query string (e.g., `/api/users?id=1` → `/api/users`).
3. **Ignores static assets** (paths ending with `.css`, `.js`, `.png`, `.jpg`, `.jpeg`, `.gif`, `.svg`, `.ico`).
4. Groups by normalized path and computes for each path:

   * `count`: number of requests
   * `p95_ms`: 95th percentile of `$request_time` in **milliseconds**
     Use the **nearest-rank** method: index = `ceil(0.95 * k)` for `k` samples.
   * `error_rate`: percentage of **5xx** responses (server errors), to two decimals
5. Returns the **top N endpoints by `p95_ms` (desc)**. Break ties by `count` (desc).
6. Output format (list of dicts), e.g.:

   ```python
   [
     {"endpoint": "/api/login", "count": 3, "p95_ms": 400, "error_rate": 33.33},
     {"endpoint": "/api/users", "count": 5, "p95_ms": 300, "error_rate": 20.00}
   ]
   ```

### Constraints / Notes

* `$request_time` is in **seconds**; convert to **milliseconds** and round to the nearest integer for `p95_ms`.
* Be resilient to extra spaces and odd user-agents.
* Lines that don’t parse should be safely skipped.
* Do not use external libraries (standard library only).

### Bonus

* Also compute `p50_ms` and `p99_ms`.
* Add an option to exclude **4xx** from the dataset when computing percentiles (sometimes useful when focusing on successful paths).
'''
import re
import math

def p95_ms(request_times_seconds):
    if not request_times_seconds:
        return None
    ms = sorted(int(round(t*1000)) for t in request_times_seconds)
    idx = math.ceil(0.95 * len(ms)) - 1  # convert to 0-based
    return ms[idx]

def error_percentage(response_codes):
    error_count = 0
    for code in response_codes:
        if code >= 500:
            error_count += 1
    return round(error_count / len(response_codes) * 100, 2)

def top_slow_endpoints(log_text: str, n: int) -> list[dict]:
    ans = []
    paths = {}
    lines = log_text.strip().splitlines()
    for line in lines:
        if any(x in line for x in ['.css', '.js', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico']):
            continue
        parts = line.split()
        api_path = re.sub(r"\?.*", r"", parts[6].strip())
        req_time = float(parts[10])
        error_rate = int(parts[8])
        if paths.get(api_path):
            paths[api_path]["count"] += 1
            paths[api_path]["req_time"].append(req_time)
            paths[api_path]["error_rate"].append(error_rate)
        else:
            paths[api_path] = {}
            paths[api_path]["count"] = 1
            paths[api_path]["req_time"] = [req_time]
            paths[api_path]["error_rate"] = [error_rate]
    for key,value in paths.items():
        for k,v in value.items():
            if k == "count":
                count = v
            elif k == "req_time":
                req_time = p95_ms(v)
            elif k == "error_rate":
                error_rate = error_percentage(v)
        ans.append(
            {"endpoint": key, "count": count, "p95_ms": req_time, "error_rate": error_rate}
        )
    print(sorted(ans, key=lambda x: x["p95_ms"] in ans)[::-1][:n])



data = """
10.0.0.1 - - [12/Sep/2025:18:50:01 +0000] "GET /api/users?id=1 HTTP/1.1" 200 123 0.120 "-" "curl/8.0"
10.0.0.2 - - [12/Sep/2025:18:50:02 +0000] "GET /api/users?id=2 HTTP/1.1" 200 150 0.240 "-" "curl/8.0"
10.0.0.3 - - [12/Sep/2025:18:50:03 +0000] "GET /api/users?id=3 HTTP/1.1" 500 50 0.300 "-" "curl/8.0"
10.0.0.4 - - [12/Sep/2025:18:50:04 +0000] "POST /api/login HTTP/1.1" 401 20 0.050 "-" "curl/8.0"
10.0.0.5 - - [12/Sep/2025:18:50:05 +0000] "POST /api/login HTTP/1.1" 200 20 0.070 "-" "curl/8.0"
10.0.0.6 - - [12/Sep/2025:18:50:06 +0000] "GET /static/app.js HTTP/1.1" 200 2048 0.005 "-" "curl/8.0"
10.0.0.7 - - [12/Sep/2025:18:50:07 +0000] "GET /api/users?id=4 HTTP/1.1" 200 120 0.180 "-" "curl/8.0"
10.0.0.8 - - [12/Sep/2025:18:50:08 +0000] "GET /api/users?id=5 HTTP/1.1" 200 110 0.090 "-" "curl/8.0"
10.0.0.9 - - [12/Sep/2025:18:50:09 +0000] "GET /favicon.ico HTTP/1.1" 200 300 0.002 "-" "curl/8.0"
10.0.0.10 - - [12/Sep/2025:18:50:10 +0000] "POST /api/login HTTP/1.1" 500 20 0.400 "-" "curl/8.0"""

top_slow_endpoints(data, 3)