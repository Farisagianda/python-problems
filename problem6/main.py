'''
6. Reverse Proxy Log Processing
Problem:
You have a log file with reverse proxy request times (in ms).
Write a function to calculate the 95th percentile of response times.

Example Input:

response_times = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

Expected Output:

950  # 95th percentile value
'''

import numpy as np

def main():
    with open("test.log", "r") as f:
        line = f.readline()
    l = line.strip("[").strip("]").split(", ")
    a = list(map(int, l))
    p95 = np.percentile(np.array(a), 95)
    print(p95)


if __name__ == "__main__":
    main()