def main(p, n):
    ans = sorted(p, key=lambda x: x["memory"], reverse=True)
    print(ans[:N])


if __name__ == "__main__":
    processes = [
        {"name": "nginx", "memory": 150},
        {"name": "mysql", "memory": 1200},
        {"name": "python", "memory": 800},
        {"name": "java", "memory": 400},
    ]
    N = 2
    main(processes, N)