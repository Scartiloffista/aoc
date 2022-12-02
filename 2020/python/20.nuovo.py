import pathlib
import math


def create_sides(tile):
    upside = tile[0]
    downside = tile[-1]
    leftside = "".join([line[0] for line in tile])
    rightside = "".join([line[-1] for line in tile])

    return [upside, downside, leftside, rightside]


path = pathlib.Path(".").parent / "inputs/20.txt.test"
with open(path, "r") as f:
    input_tiles_raw = f.read().split("\n\n")

tiles = {}
list_of_sides = []

for tile in input_tiles_raw:
    temp = tile.splitlines()
    number = int(temp[0].split(" ")[1][:-1])
    tile = temp[1:]
    tiles[number] = tile
    list_of_sides += create_sides(tile)

count_of_sides_with_no_neigh_for_tile = {}

for i, tile in tiles.items():
    count_of_sides_with_no_neigh = 0
    # generate sides
    sides = create_sides(tile)
    for side in sides:
        count_occurrences = list_of_sides.count(side)
        count_occurrences += list_of_sides.count(side[::-1])
        if count_occurrences < 2:
            count_of_sides_with_no_neigh += 1

    count_of_sides_with_no_neigh_for_tile[i] = count_of_sides_with_no_neigh

listt = [k for k, v in count_of_sides_with_no_neigh_for_tile.items() if v == 2]
val = math.prod(listt)
print(val)
