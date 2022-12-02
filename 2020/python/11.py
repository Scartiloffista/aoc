import os
import pathlib
import copy

path = pathlib.Path('.').parent / "inputs/11.test.txt"
with open(path, "r") as f:
    char_map = f.read().splitlines()

max_rows = len(char_map)
max_cols = len(char_map[0])

def is_occupied(char):
    return char == '#'

def can_be_changed(char_map, i, j):
    counter_occupied = 0
    if i>0 and is_occupied(char_map[i-1][j]):
        ## up
        counter_occupied += 1
    if i>0 and j<(max_cols-1) and is_occupied(char_map[i-1][j+1]):
        ## up_right
        counter_occupied += 1
    if i>0 and j>0 and is_occupied(char_map[i-1][j-1]):
        ## up_left
        counter_occupied += 1
    if j>0 and is_occupied(char_map[i][j-1]):
        ## left
        counter_occupied += 1
    if j<(max_cols-1) and is_occupied(char_map[i][j+1]):
        ## right
        counter_occupied += 1
    if i<(max_rows-1) and is_occupied(char_map[i+1][j]):
        ## down
        counter_occupied += 1
    if i<(max_rows-1) and j>0 and is_occupied(char_map[i+1][j-1]):
        ## down_left
        counter_occupied += 1
    if i<(max_rows-1) and j<(max_cols-1) and is_occupied(char_map[i+1][j+1]):
        ## down_right
        counter_occupied += 1
    
    if char_map[i][j] == 'L' and counter_occupied == 0:
        return '#'
    elif char_map[i][j] == '#' and counter_occupied >= 4:
        return 'L'
    else:
        return char_map[i][j]

def evaluate(char_map):
    """
    docstring
    """
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
    if char_map == old_map:
        break

occupied = sum([1 for sublist in char_map for item in sublist if item == '#'])
print(occupied)