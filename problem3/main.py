def main(r, n):
    ans = []
    for i in r:
        if i["response_time"] >= 500:
            ans.append(i)
    #ans = sorted(ans, key=lambda x: x["response_time"], reverse=True)
    print(ans)




if __name__ == "__main__":
    requests = [
        {"endpoint": "/api/v1/login", "response_time": 200},
        {"endpoint": "/api/v1/data", "response_time": 800},
        {"endpoint": "/api/v1/status", "response_time": 1000},
        {"endpoint": "/api/v1/users", "response_time": 400},
    ]
    threshold = 500
    main(requests, threshold)