"""
Analyzes a log file to find the top 5 most active IP addresses.

Args:
    file_path (str): The path to the log file.

Returns:
    A list of tuples, where each tuple contains the IP address and its count,
    sorted in descending order of count. Returns an empty list on error.

Example log file (access.log):
127.0.0.1 - - [24/Sep/2025:10:00:01 -0700] "GET /index.html HTTP/1.1" 200 1024
192.168.1.10 - - [24/Sep/2025:10:00:02 -0700] "GET /images/logo.png HTTP/1.1" 200 5120
127.0.0.1 - - [24/Sep/2025:10:00:03 -0700] "GET /styles/main.css HTTP/1.1" 200 2048
10.0.0.5 - - [24/Sep/2025:10:00:04 -0700] "POST /api/data HTTP/1.1" 201 100
192.168.1.10 - - [24/Sep/2025:10:00:05 -0700] "GET /images/logo.png HTTP/1.1" 200 5120
127.0.0.1 - - [24/Sep/2025:10:00:06 -0700] "GET /index.html HTTP/1.1" 200 1024
10.0.0.5 - - [24/Sep/2025:10:00:07 -0700] "GET /api/status HTTP/1.1" 200 50
127.0.0.1 - - [24/Sep/2025:10:00:08 -0700] "GET /index.html HTTP/1.1" 200 1024
"""
import argparse

def top_5_ipaddress(logfile):
    ipaddress_count = {}
    ans = []
    try:
        with open(logfile, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                parts = line.split()
                if len(parts) == 0:
                    continue
                ipaddress = parts[0]
                if ipaddress_count.get(ipaddress):
                    ipaddress_count[ipaddress] += 1
                else:
                    ipaddress_count[ipaddress] = 1
    except FileNotFoundError:
        print("Error. File not found.")
        return []
    except PermissionError:
        print("Error. File cannot be read.")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []
    ans = sorted(ipaddress_count.items(), key=lambda x: x[1], reverse=True)[:5]
    return ans

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--logfile", default="access.log", type=str)
    args = parser.parse_args()
    print(top_5_ipaddress(args.logfile))