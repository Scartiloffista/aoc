import pathlib

path = pathlib.Path(".").parent / "inputs/20.txt.test"
with open(path, "r") as f:
    tiles = f.read().split("\n\n")


def evaluate_tile(tile, number, dict_of_sides):
    upside = tile[0]
    downside = tile[-1]
    leftside = "".join([line[0] for line in tile])
    rightside = "".join([line[-1] for line in tile])

    if dict_of_sides.get(upside, None) is None:
        dict_of_sides[upside] = [number]
    else:
        dict_of_sides[upside].append(number)

    if dict_of_sides.get(downside, None) is None:
        dict_of_sides[downside] = [number]
    else:
        dict_of_sides[downside].append(number)

    if dict_of_sides.get(leftside, None) is None:
        dict_of_sides[leftside] = [number]
    else:
        dict_of_sides[leftside].append(number)

    if dict_of_sides.get(rightside, None) is None:
        dict_of_sides[rightside] = [number]
    else:
        dict_of_sides[rightside].append(number)

dict_of_sides = {}
histogram = {}
for tile in tiles:
    temp = tile.splitlines()
    number = int(temp[0].split(" ")[1][:-1])
    histogram[number] = 0
    tile = temp[1:]
    evaluate_tile(tile, number, dict_of_sides)

list_of_val = []

# for i, k in dict_of_sides.items():
#     if i[::-1] in dict_of_sides:
        

sett = set(list_of_val)
print("ciao")
