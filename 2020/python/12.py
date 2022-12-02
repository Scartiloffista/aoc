import os
import pathlib
import copy

path = pathlib.Path('.').parent / "inputs/12.txt"
with open(path, "r") as f:
    instructions = f.read().splitlines()

directions = ["N", "E", "S", "W"]
instructions = [[x[:1], int(x[1:])] for x in instructions]

curr_direction = "E"
curr_pos = [0,0]

for (index,(instr, n)) in enumerate(instructions):
    if instr == "F":
        instr = curr_direction

    if instr == "N":
        curr_pos[0] += n
    elif instr == "E":
        curr_pos[1] += n
    elif instr == "S":
        curr_pos[0] -= n
    elif instr == "W":
        curr_pos[1] -= n
    elif instr == "R":
        incr = n//90
        curr_direction = directions[(directions.index(curr_direction) + incr) % 4]
    elif instr == "L":
        incr = n//90
        curr_direction = directions[(directions.index(curr_direction) - incr) % 4]
        

print(abs(curr_pos[0]) + abs(curr_pos[1]))

