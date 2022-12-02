import pathlib
import os

path = pathlib.Path('.').parent / "inputs/6.txt"
with open(path, "r") as f:
    groups = f.read().split("\n\n")

count = 0
for group in groups:
    list_of_responses = [set(a) for a in group.split("\n")]
    intersection = set.intersection(*list_of_responses)

    count += len(intersection)

print(count)