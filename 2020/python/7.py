import pathlib
import os

path = pathlib.Path('.').parent / "inputs/7.txt"
with open(path, "r") as f:
    input_lines = f.read()

rules = input_lines.split("\n")
rules = [a for a in rules if not a.startswith("shiny gold bag")]
count = 1
valid_bags = [a for a in rules if "shiny gold bag" in a]
already_checkec_bags = []
already_checkec_bags += valid_bags

while len(valid_bags) > 0:
    bags = valid_bags
    valid_bags = []
    for bag in bags:
        bag = bag.split(" ")[:3]
        bag = " ".join(bag)[:-1]
        new_bags = [a for a in rules if bag in a and not a.startswith(bag) and a not in already_checkec_bags]
        valid_bags += new_bags
    already_checkec_bags += valid_bags
    
print(len(set(already_checkec_bags)))