
def main():
    count = 0
    endpoint = []
    with open("test.log", "r") as f:
        lines = f.readlines()
        for line in lines:
            if "ERROR" in line:
                count += 1
                if "endpoint" in line:
                    l = line.split()
                    endpoint.append(l[l.index("endpoint") + 1])
    print(f"Total ERROR logs: {count}")
    print(f"Endpoints with errors: {endpoint}")


if __name__ == "__main__":
    main()