"""
🛰 4. Check Hazardous Asteroids for the Week
Description:
Create a CLI that checks for only potentially hazardous asteroids for a given week.

CLI Usage:

python hazardous.py --week-of 2025-04-01
Requirements:

Use --week-of as the start date

Print asteroid names and miss distances

Highlight any with a miss distance < 1 million km
"""
import requests
import sys
import argparse
from datetime import datetime, timedelta

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--week-of", type=str, required=True)
    parser.add_argument("--apikey", type=str, default="DEMO_KEY")
    args = parser.parse_args()
    date_obj = datetime.strptime(args.week_of, "%Y-%m-%d").date()
    week_end = date_obj + timedelta(days=7)
    #print(week_end)

    request = requests.get(f"https://api.nasa.gov/neo/rest/v1/feed?start_date={args.week_of}&end_date={week_end}&api_key={args.apikey}")
    if request.status_code != 200:
        print("Error calling nasa neow API")
        print(f"Response: {request.text}")
        sys.exit(1)
    json_data = request.json()
    #print(json_data)
    neo = json_data['near_earth_objects']
    for date in neo:
        for asteroid in neo[date]:
            name = asteroid['name']
            close_approach_data = asteroid['close_approach_data']
            miss_distance = float(close_approach_data[0]["miss_distance"]["kilometers"])
            #print(asteroid)
            #print(miss_distance)
            if asteroid["is_potentially_hazardous_asteroid"] == True and miss_distance >= 10**6:
                print(f"Name: {name}, Miss distance: {miss_distance}km")
            elif asteroid["is_potentially_hazardous_asteroid"] == True and miss_distance < 10**6:
                print(f"Name: {name}, Miss distance: {miss_distance}km  -> Hazardous!")
            else:
                print("No potentially hazardous asteroid found.")
main()