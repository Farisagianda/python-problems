"""
☄️ 2. Find the Closest Asteroid in a Date Range
Description:
Write a script that accepts --start-date and --end-date and finds the asteroid that passed closest to Earth during that time.

CLI Usage:

python closest_asteroid.py --start-date 2025-04-01 --end-date 2025-04-07
Requirements:

Use argparse for --start-date and --end-date

Sort asteroids by miss distance and print the closest one
"""
import argparse
import requests
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-date", type=str, required=True)
    parser.add_argument("--end-date", type=str, required=True)
    parser.add_argument("--apikey", type=str, default="DEMO_KEY")
    args = parser.parse_args()
    output = []
    request = requests.get(f"https://api.nasa.gov/neo/rest/v1/feed?start_date={args.start_date}&end_date={args.end_date}&api_key={args.apikey}")
    if request.status_code != 200:
        print("Problem getting API response from NASA API")
        print(f"Response: {request.text}")
        sys.exit(1)
    json_data = request.json()
    objects = json_data["near_earth_objects"]
    for date in objects:
        asteroids = objects[date]
        for asteroid in asteroids:
            name = asteroid["name"]
            close_approach = asteroid["close_approach_data"]
            miss_distance_str = close_approach[0]["miss_distance"]["kilometers"]
            try:
                miss_distance = float(miss_distance_str)
            except ValueError as e:
                print(f"Converting miss_distance to float failed with: {e}")
                continue
            data = {"name": name, "miss_distance": miss_distance}
            output.append(data)
    if not output:
        print("No asteroids data found.")
        sys.exit(0)
    sorted_output = sorted(output, key=lambda x: x["miss_distance"])
    print(sorted_output[0])
    #out = [f"{x}" for x in sorted_output]


if __name__ == "__main__":
    main()