def main(lines, n):
    ans = []
    for l in set(lines):
        c = lines.count(l)
        ans.append((l, c))
    ans = sorted(ans, key=lambda x: x[1], reverse=True)
    print(ans[:n])




if __name__== "__main__":
    logs = [
        "Database connection failed",
        "Service crashed at endpoint /api/v1/users",
        "Database connection failed",
        "Memory leak detected",
        "Service crashed at endpoint /api/v1/users",
        "Service crashed at endpoint /api/v1/users",
    ]
    n = 2
    main(logs, n)
