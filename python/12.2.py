import os
import pathlib
import copy

def rotate(l, n):
    return l[n:] + l[:n]

path = pathlib.Path('.').parent / "inputs/12.txt"
with open(path, "r") as f:
    instructions = f.read().splitlines()

instructions = [[x[:1], int(x[1:])] for x in instructions]

waypoint = [1, 10]
current_pos = [0,0]

for (index,(instr, n)) in enumerate(instructions):
    x, y = current_pos
    if instr == 'F':
        current_pos = [x + waypoint[0]*n, y + waypoint[1]*n]
    elif instr == "E":
        waypoint[1] += n
    elif instr == "S":
        waypoint[0] -= n
    elif instr == "W":
        waypoint[1] -= n
    elif instr == 'N':
        waypoint[0] += n
    elif instr == "R":
        incr = n//90
        for i in range(incr):
            waypoint = rotate(waypoint, 1)
            waypoint[0] = -waypoint[0]
    elif instr == "L":
        incr = (360-n)//90
        for i in range(incr):
            waypoint = rotate(waypoint, 1)
            waypoint[0] = -waypoint[0]

print(abs(current_pos[0]) + abs(current_pos[1]))