"""🪐 5. Interactive Asteroid Detail Lookup
Description:
Pass an asteroid ID or name via command line and fetch its full details.

CLI Usage:

python asteroid_info.py --id 3542519
Requirements:

Use this endpoint: https://api.nasa.gov/neo/rest/v1/neo/{asteroid_id}

Print orbiting body, close approaches, velocity, etc."""
import requests
import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", type=int)
    parser.add_argument("--name", type=str)
    parser.add_argument("--apikey", type=str, default="DEMO_KEY")
    args = parser.parse_args()
    request = requests.get(f"https://api.nasa.gov/neo/rest/v1/neo/{args.id}?api_key={args.apikey}")
    if request.status_code != 200:
        print("Error calling NASA Neo API")
        print(f"Response: {request.text}")
        sys.exit(1)
    json_data = request.json()
    name = json_data['name']
    close_approach_data = json_data['close_approach_data']
    print(f"{name} asteroid infos below")
    for data in close_approach_data:
        close_approach_date = data['close_approach_date']
        relative_velocity_per_s = round(float(data['relative_velocity']['kilometers_per_second']), 3)
        orbiting_body = data['orbiting_body']
        miss_distance_km = round(float(data['miss_distance']['kilometers']), 3)
        print(f"  Orbiting body: {orbiting_body}, close approach date: {close_approach_date}, relative velocity: {relative_velocity_per_s} km/s, miss distance: {miss_distance_km} km")

main()