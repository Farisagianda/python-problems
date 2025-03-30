import bisect

def main_module(s):
    ans = bisect.bisect_right(sorted(list(s.values())), 80)
    if ans == len(s):
        print("OK")
    else:
        print("ALERT")

def main(s):
    if sorted(list(s.values()))[-1] > 80:
        print("ALERT")
    else:
        print("OK")

if __name__ == "__main__":
    system_status = {
        "cpu": 75,
        "memory": 85,
        "disk": 60
    }
    main(system_status)