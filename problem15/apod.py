"""
🌌 3. Check the Astronomy Picture of the Day (APOD)
Description:
Write a CLI tool that gets the NASA Astronomy Picture of the Day.

CLI Usage:

python apod.py [--date YYYY-MM-DD]
Requirements:

If no date is passed, default to today

Print the title, date, and explanation

Optionally show the image URL or download it
"""
import requests
import argparse
from datetime import date
import sys

def main():
    today = date.today().strftime("%Y-%m-%d")
    parser = argparse.ArgumentParser()
    parser.add_argument("--apikey", type=str, default="DEMO_KEY")
    parser.add_argument("--date", type=str, default=today)
    parser.add_argument("--download", action='store_true', help='If specificed, will download the image locally to apod.jpeg file.')
    args = parser.parse_args()

    request = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={args.apikey}&date={args.date}")
    if request.status_code != 200:
        print("Error calling NASA's apod API")
        print(f"Response: {request.text}")
        sys.exit(1)
    json_data = request.json()
    title = json_data['title']
    date_now = json_data['date']
    explanation = json_data['explanation']
    img_url = json_data['url']
    output = f"Title: {title}\nDate: {date_now}\nExplanation:\n  {explanation}\nImage URL: {img_url}."
    if args.download:
        try:
            img_data = requests.get(img_url).content
            with open("apod.jpeg", "wb") as handler:
                handler.write(img_data)
            print(output)
            print(f"Image from {img_url} downloaded to apod.jpeg")
        except Exception as e:
            print(f"Error downloading the image: {e}")
    else:
        print(output)

main()