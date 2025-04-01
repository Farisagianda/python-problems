"""
Extract Disk Space Info from df -h Output
A system administrator runs df -h and gets this output:


Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       100G   75G   25G  75% /
/dev/sdb1       500G  320G  180G  64% /data
Write a function that:

Extracts Filesystem, Size, and Used columns.

Returns a list of dictionaries.

Expected Output:
[
    {"filesystem": "/dev/sda1", "size": "100G", "used": "75G"},
    {"filesystem": "/dev/sdb1", "size": "500G", "used": "320G"}
]

"""

def main(n):
    ans = []
    parts = [l.split() for l in n.strip().split('\n')]
    header = parts[0]
    content = parts[1:]
    for line in content:
        d = {}
        for i,v in enumerate(header):
            if v == 'Filesystem' or v == 'Size' or v == 'Used':
                d[v.lower()] = line[i]
        ans.append(d)
    print(ans)



n = """
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       100G   75G   25G  75% /
/dev/sdb1       500G  320G  180G  64% /data"""


main(n)