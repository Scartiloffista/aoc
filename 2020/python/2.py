import pathlib
import os

path = pathlib.Path('.').parent / "inputs/2.txt"
with open(path, "r") as f:
    input_list = f.read().splitlines()

counter = 0

for i in input_list:
    rule, password = i.split(":")
    nums, char = rule.split(" ")
    pos1, pos2 = nums.split("-")
    pos1 = int(pos1)
    pos2 = int(pos2)
    if((password[pos1] == char) ^ (password[pos2] == char)):
        counter += 1

print(counter)
