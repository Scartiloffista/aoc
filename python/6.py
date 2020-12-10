import pathlib
import os

path = pathlib.Path('.').parent / "inputs/6.txt"
with open(path, "r") as f:
    groups = f.read().split("\n\n")

count = 0

for group in groups:
    group = (set(group.replace("\n", "")))
    count += len(group)
    
print(count)