"""
 Process JSON API Response and Extract Key Data
A monitoring system provides JSON API responses:

{
    "status": "OK",
    "metrics": {
        "cpu_usage": "78%",
        "memory_usage": "65%",
        "disk_free": "120GB"
    },
    "alerts": []
}
Write a function that:

Extracts cpu_usage and memory_usage as integers (remove %).

Returns a dictionary with numerical values.

Expected Output:
{"cpu_usage": 78, "memory_usage": 65}
"""
import json

def main():
    d = {}
    with open("test.json", "r") as jsonfile:
        data = json.load(jsonfile)
    d["cpu_usage"] = int(data["metrics"]["cpu_usage"].strip("%"))
    d["memory_usage"] = int(data["metrics"]["memory_usage"].strip("%"))
    print(d)
main()