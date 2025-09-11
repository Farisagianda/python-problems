"""
Problem:

You’re tasked with writing a Python function to monitor and report disk usage for each mount point on a Linux server.

Requirements:

No external libraries (use only Python’s built-in modules).

Return a dictionary where:

The keys are mount points (e.g., /, /home, /var/log).

The values are tuples containing:

total size in GB (rounded to 2 decimal places)

used size in GB (rounded to 2 decimal places)

percentage used (integer).

The function should ignore special filesystems like tmpfs, proc, sysfs, and any mount points under /run.

Optimize for clarity and performance.

Include a quick way to detect if any mount point exceeds 80% usage.

Example Output:

{
    "/": (50.0, 35.5, 71),
    "/home": (200.0, 180.0, 90)
}
# High usage: ['/home']
"""

def utilization_checker(mount_data):
    for data in mount_data:
        mount_point = data.keys()
        print(mount_point)

utilization_checker()
