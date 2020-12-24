import pathlib
import re
import copy
import operator

path = pathlib.Path(".").parent / "inputs/24.txt"
with open(str(path), "r") as f:
    lines = f.read().splitlines()

dict_of_moves = {
    "e": (0, 2),
    "w": (0, -2),
    "se": (-1, 1),
    "sw": (-1, -1),
    "nw": (1, -1),
    "ne": (1, 1),
}


def apply_day(tiles):
    dict_with_new_neighs = {}

    for pos, colour in tiles.items():
        # dict_with_new_neighs[pos] = tiles[pos]
        for move in dict_of_moves.values():

            new_pos = tuple(map(operator.add, pos, move))
            adj = tiles.get(new_pos, None)
            if not adj:
                dict_with_new_neighs[new_pos] = "w"

    dict_with_new_neighs = {**dict_with_new_neighs, **tiles}
    new_dict = {}

    for pos, colour in dict_with_new_neighs.items():
        col_neighs = ""

        for move in dict_of_moves.values():

            new_pos = tuple(map(operator.add, pos, move))
            adj = dict_with_new_neighs.get(new_pos, None)
            if not adj:
                new_dict[new_pos] = "w"
                col_neighs += "w"
            else:
                col_neighs += dict_with_new_neighs.get(new_pos)

        if colour == "b" and (col_neighs.count("b") == 0 or col_neighs.count("b") > 2):
            new_dict[pos] = "w"
        elif colour == "w" and col_neighs.count("b") == 2:
            new_dict[pos] = "b"
        else:
            new_dict[pos] = colour

    return new_dict


dict_of_tiles = {(0, 0): "w"}

for line in lines:
    pos = (0, 0)
    for match in re.finditer(r"(e|se|sw|w|nw|ne)", line):
        start = match.start()
        end = match.end()
        instr = line[start:end]
        move = dict_of_moves[instr]
        pos = tuple(map(operator.add, pos, move))

    color = dict_of_tiles.get(pos, "w")
    if color == "b":
        dict_of_tiles[pos] = "w"
    else:
        dict_of_tiles[pos] = "b"

count = sum([1 for x in dict_of_tiles.values() if x == "b"])
print(count)

new_tiles = dict_of_tiles

for i in range(100):

    new_tiles = apply_day(new_tiles)
    count = sum([1 for x in new_tiles.values() if x == "b"])

count = sum([1 for x in new_tiles.values() if x == "b"])
print(count)