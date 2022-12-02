import os
import pathlib
import copy

path = pathlib.Path('.').parent / "inputs/11.txt"
with open(path, "r") as f:
    char_map = f.read().splitlines()

max_rows = len(char_map)
max_cols = len(char_map[0])

def can_see_occupied(i, j, i_i ,i_j):
    while 0<=i<max_rows and 0<=j<max_cols:# and not flag:
        i += i_i
        j += i_j
        if 0<=i<max_rows and 0<=j<max_cols:
            if char_map[i][j] == '.':
                continue
            elif char_map[i][j] == 'L':
                return False
            else:
                return True

def can_be_changed(char_map, i, j):
    counter_occupied = 0
    if i>0 and can_see_occupied(i, j, -1, 0):
        ## up
        counter_occupied += 1
    if i>0 and j<(max_cols-1) and can_see_occupied(i, j, -1, +1):
        ## up_right
        counter_occupied += 1
    if i>0 and j>0 and can_see_occupied(i, j, -1, -1):
        ## up_left
        counter_occupied += 1
    if j>0 and can_see_occupied(i, j, 0, -1):
        ## left
        counter_occupied += 1
    if j<(max_cols-1) and can_see_occupied(i, j, 0, +1):
        ## right
        counter_occupied += 1
    if i<(max_rows-1) and can_see_occupied(i, j, +1, 0):
        ## down
        counter_occupied += 1
    if i<(max_rows-1) and j>0 and can_see_occupied(i, j, +1, -1):
        ## down_left
        counter_occupied += 1
    if i<(max_rows-1) and j<(max_cols-1) and can_see_occupied(i, j, +1, +1):
        ## down_right
        counter_occupied += 1
    
    if char_map[i][j] == 'L' and counter_occupied == 0:
        return '#'
    elif char_map[i][j] == '#' and counter_occupied >= 5:
        return 'L'
    else:
        return char_map[i][j]

def evaluate(char_map):
    new_map = []
    for i in range(max_rows):
        row = ""
        for j in range(max_cols):
            row += can_be_changed(char_map, i,j)
        new_map += [row]
    return new_map

count = 0
while True:
    count += 1
    old_map = copy.deepcopy(char_map)
    char_map = evaluate(char_map)
    # for i in char_map:
    #     print(i)
    if char_map == old_map:
        break

occupied = sum([1 for sublist in char_map for item in sublist if item == '#'])
print(occupied)