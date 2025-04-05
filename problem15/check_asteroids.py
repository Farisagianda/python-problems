"""
1. Check for Near-Earth Asteroids on a Given Date
Description:
Write a script that accepts a date via command-line and prints the list of near-Earth asteroids that were close to Earth on that day using NASA’s NeoWs API.

CLI Usage:

python check_asteroids.py --date 2025-04-01
Requirements:

Use argparse to accept --date

Fetch from: https://api.nasa.gov/neo/rest/v1/feed

Display name, estimated diameter, miss distance (km), and whether it’s potentially hazardous
"""
import requests
import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", help="date for input", type=str, required=True)
    parser.add_argument("--apikey", help="api key for nasa API call", type=str, default="DEMO_KEY")
    args = parser.parse_args()
    request = requests.get(f"https://api.nasa.gov/neo/rest/v1/feed?start_date={args.date}&end_date={args.date}&api_key={args.apikey}")
    if request.status_code != 200:
        print("Error fetching data from NASA API.")
        print(f"Response: {request.text}")
        sys.exit(1)
    json_data = request.json()
    for item in json_data["near_earth_objects"][args.date]:
        estimated_diameter = (item["estimated_diameter"]["meters"]["estimated_diameter_min"] + item["estimated_diameter"]["meters"]["estimated_diameter_max"]) / 2
        estimated_diameter = round(estimated_diameter, 3)
        print(f'Display name: {item["name"]}, estimated diameter: {str(estimated_diameter)}m, miss distance: {item["close_approach_data"][0]["miss_distance"]["kilometers"]}km, potentially hazardous: {item["is_potentially_hazardous_asteroid"]}')


if __name__ == "__main__":
    main()
