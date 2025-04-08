import argparse
import sys

"""1. Dinosaur with the Largest and Smallest Feet
Problem:
Given a CSV file containing dinosaur details (with columns such as "Name", "Foot Length", "Weight", "Diet", etc.), write a script that:

Reads the CSV file.

Finds and prints the details of the dinosaur with the largest foot length.

Finds and prints the details of the dinosaur with the smallest foot length."""

def feet_size(dino_info):
    sort_by_feet = sorted(dino_info, key=lambda x: int(x['Foot Length']))
    print("Dinosaur with Largest Foot Length:")
    print(", ".join([f"{key}: {value}" for key, value in sort_by_feet[-1].items()]))
    print("\nDinosaur with Smallest Foot Length:")
    print(", ".join([f"{key}: {value}" for key, value in sort_by_feet[0].items()]))

"""
2. Filter Dinosaurs by Foot Size Threshold
Problem:
Write a script that:

Accepts a CSV file of dinosaur data.

Allows the user to input a foot length threshold (via command-line argument).

Prints the details of all dinosaurs with a foot length greater than the given threshold (i.e., "big feet" dinosaurs)."""

def foot_threshold(dino_info, threshold):
    print(f"Dinosaurs with bigger than {str(threshold)}cm foot")
    found = False
    for dino in dino_info:
        if int(dino["Foot Length"]) > threshold:
            data = ", ".join([f"{key}: {value}" for key, value in dino.items()])
            print(data)
            found = True
    if not found:
        print(f"No dinosaurs with bigger than {str(threshold)}cm foot!")

"""
3. Group and Compare by Diet
Problem:
Create a script that:

Reads dinosaur data from a CSV file.

Groups the dinosaurs by their diet (e.g., Carnivore, Herbivore, Omnivore).

For each diet group, calculates and prints the average foot length.

Additionally, prints the dinosaur with the maximum foot length in each diet group.
"""
def group_by_diet(dino_info):
    carn_foot_lengths, herb_foot_lengths, omn_foot_lengths = [], [], []
    for dino in dino_info:
        if not dino["Diet"]:
            print(f"Diet category is empty for dino {dino['Name']}")
            continue
        if dino["Diet"].lower() == "carnivore":
            carn_foot_lengths.append(int(dino["Foot Length"].strip()))
        elif dino["Diet"].lower() == "herbivore":
            herb_foot_lengths.append(int(dino["Foot Length"].strip()))
        else:
            omn_foot_lengths.append(int(dino["Foot Length"].strip()))
    if carn_foot_lengths:
        print(f"Carnivores average foot length: {sum(carn_foot_lengths)/len(carn_foot_lengths)}cm")
        print(f"Carnivore maximum foot length in the group: {round(max(carn_foot_lengths),3)}cm\n")
    if herb_foot_lengths:
        print(f"Herbivores average foot length: {round(sum(herb_foot_lengths)/len(herb_foot_lengths),3)}cm")
        print(f"Herbivore maximum foot length in the group: {round(max(herb_foot_lengths),3)}cm\n")
    if omn_foot_lengths:
        print(f"Omnivores average foot length: {sum(omn_foot_lengths)/len(omn_foot_lengths)}cm")
        print(f"Omnivore maximum foot length in the group: {round(max(omn_foot_lengths),3)}cm")

"""
4. Sort and Rank Dinosaurs by Foot Length
Problem:
Develop a script that:

Reads a CSV file containing dinosaur information.

Sorts the dinosaurs by foot length in descending order.

Displays the top N dinosaurs with the largest feet, where N is a parameter provided by the user (using argparse).
"""
def top_large_feet(dino_info, n):
    sorted_reverse = sorted(dino_info, key=lambda x: int(x["Foot Length"].strip()), reverse=True)
    if n < 0:
        return
    if n >= len(sorted_reverse):
        n = len(sorted_reverse)
    top_n = sorted_reverse[:n]
    print(f"Top {n} large feet dinosaurs:")
    for dino in top_n:
        print(", ".join([f"{key}: {value}" for key,value in dino.items()]))



def main():
    dino_info = []
    parser = argparse.ArgumentParser()
    parser.add_argument("--csvfile", default="dinosaurs.csv", type=str)
    parser.add_argument("--check-feet-size", action="store_true")
    parser.add_argument("--foot-threshold", type=int)
    parser.add_argument("--group-by-diet", action="store_true")
    parser.add_argument("--top-large-feet", type=int)
    args = parser.parse_args()
    with open(args.csvfile, "r") as file:
        data = file.read()
    data = data.split('\n')
    headers = data[0].split(",")
    dino_data = data[1:]
    for dino in dino_data:
        if not dino.strip():
            continue
        dino_dict = {}
        dino_list = dino.split(',')
        for index, header in enumerate(headers):
            dino_dict[header] = dino_list[index]
        dino_info.append(dino_dict)
    if args.check_feet_size:
        feet_size(dino_info)
    if args.foot_threshold:
        foot_threshold(dino_info, args.foot_threshold)
    if args.group_by_diet:
        group_by_diet(dino_info)
    if args.top_large_feet:
        top_large_feet(dino_info, args.top_large_feet)

main()