import pathlib
import os

path = pathlib.Path('.').parent / "inputs/7.txt"
with open(path, "r") as f:
    input_lines = f.read()

rules = input_lines.split("\n")
initial = [a for a in rules if a.startswith("shiny gold bag")][0]
rules = [a for a in rules if not a.startswith("shiny gold bag")]

def evaluate(bag):
    bag = bag.replace(".", "")
    inside_bags = bag.split(" contain ")[1].split(", ")
    count = 1
    for bag in inside_bags:
        if bag == "no other bags":
            continue
        multiplier = int(bag[0])
        bag = [a for a in rules if a.startswith(bag[2:])][0]
        count += multiplier * evaluate(bag)
    
    return count

print(evaluate(initial)-1)