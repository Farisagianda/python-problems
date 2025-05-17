"""
2. Disk Usage Alert

Given a list of file paths and their sizes (in MB), write a function to alert if total usage exceeds a threshold.

files = [
    ("/var/log/app.log", 200),
    ("/home/user/temp.txt", 350),
    ("/var/log/sys.log", 100)
]

Task: Alert if total > 500MB.
"""
def main(files):
    if not files:
        print('File list does not exist or is empty')
        return 1
    total_size = sum(size for _,size in files)
    if total_size > 500:
        print(f"Total size of the files is {total_size}MB and exceeds the 500MB threshold.")
        return 1
    else:
        print(f"Total size is {total_size}MB and is within the 500MB threshold.")
        return 0

if __name__ == "__main__":
    files = [
        ("/var/log/app.log", 200),
        ("/home/user/temp.txt", 350),
        ("/var/log/sys.log", 100)
    ]
    main(files)
