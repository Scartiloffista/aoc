import pathlib
import re
import math


def rot_90(lst):
    ciao = ["".join(list(reversed(x))) for x in zip(*lst)]
    return ciao


def flip(lst):
    ciao = list(reversed(lst))
    return ciao


def all_rotations(lst):
    yield lst
    yield flip(lst)
    lst = rot_90(lst)  # 90
    yield lst
    yield flip(lst)
    lst = rot_90(lst)  # 180
    yield lst
    yield flip(lst)
    lst = rot_90(lst)  # 270
    yield lst
    yield flip(lst)


def create_sides(tile):
    upside = tile[0]
    downside = tile[-1]
    leftside = "".join([line[0] for line in tile])
    rightside = "".join([line[-1] for line in tile])
    return [upside, downside, leftside, rightside]


def link_tile_to_side(tile, number, dict_of_sides):
    upside, downside, leftside, rightside = create_sides(tile)

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


def remove_gaps(mapp):
    mappina = mapp[1:-1]
    new_map = []
    for line in mappina:
        new_map.append(line[1:-1])
    return new_map


def get_matching_side(side: str, tile_number: int, dict_sides: dict) -> int:
    lst_1 = dict_sides.get(side, None) or []
    lst_2 = dict_sides.get(side[::-1], None) or []
    lstt = set(lst_1 + lst_2) - set([tile_number])
    if len(lstt) == 1:
        return list(lstt)[0]
    elif len(lstt) == 0:
        return None
    else:
        raise Exception("mmmh")


def get_orientation_starting_corner(tile_number, dict_of_sides):
    tile = tiles[tile_number]
    for orr in all_rotations(tile):
        u, d, l, r = create_sides(orr)
        flagd = get_matching_side(d, tile_number, dict_of_sides)
        flagr = get_matching_side(r, tile_number, dict_of_sides)
        if flagd is not None and flagr is not None:
            return orr  # , flagd, flagr


path = pathlib.Path(".").parent / "inputs/20.txt"
with open(path, "r") as f:
    input_tiles_raw = f.read().split("\n\n")

tiles = {}
sides = {}

final_map = {}
final_placements = {}

for tile in input_tiles_raw:
    temp = tile.splitlines()
    number = int(temp[0].split(" ")[1][:-1])
    tile = temp[1:]
    tiles[number] = tile
    # now i have to link every side with its tile
    link_tile_to_side(tile, number, sides)


n_tiles_for_side = int(math.sqrt(len(tiles.keys())))
random_tile = tiles[list(tiles.keys())[0]]
n_char_for_side = len(random_tile[0])

# i know corners: [3343, 3821, 3677, 3709]
# 1951 for example

foo = get_orientation_starting_corner(3821, sides)
final_map[(0, 0)] = foo
final_placements[(0, 0)] = 3821

visited_number_debug = [3821]

for i in range(0, n_tiles_for_side):
    for j in range(0, n_tiles_for_side):
        if i == 0 == j:
            continue

        elif j == 0:
            # first item of row, taking it from above!
            previous_tile = final_map[(i - 1, j)]
            previous_number = final_placements[(i - 1, j)]

            _, d, _, _ = create_sides(previous_tile)
            new_number = get_matching_side(d, previous_number, sides)
            actual_tile = tiles[new_number]

            final_placements[(i, j)] = new_number
            if new_number in visited_number_debug:
                raise Exception("cazzo non va la ricostruzione")
            visited_number_debug.append(new_number)
            for orr in all_rotations(actual_tile):
                new_u, _, _, _ = create_sides(orr)
                if d == new_u:
                    final_map[(i, j)] = orr
                    break

        else:
            previous_tile = final_map[(i, j - 1)]
            previous_number = final_placements[(i, j - 1)]

            _, _, _, r = create_sides(previous_tile)
            new_number = get_matching_side(r, previous_number, sides)
            actual_tile = tiles[new_number]

            final_placements[(i, j)] = new_number
            if new_number in visited_number_debug:
                raise Exception("cazzo non va la ricostruzione")
            visited_number_debug.append(new_number)

            for orr in all_rotations(actual_tile):
                _, _, new_l, _ = create_sides(orr)
                if r == new_l:
                    final_map[(i, j)] = orr
                    break

# debug
flag = set(visited_number_debug) == set(tiles.keys())
print(flag)

# i = 1
for i in range(0, n_tiles_for_side):
    for j in range(0, n_tiles_for_side):
        final_map[(i, j)] = remove_gaps(final_map[(i, j)])

# making a big final map
no_gap_map = []
for i in range(0, n_tiles_for_side):
    # first row!
    # devo prima stampare le prime righe di ognuno di questi item, poi le seconde righe, etc
    for row in range(0, n_char_for_side - 2):
        strr = ""
        for j in range(0, n_tiles_for_side):
            row_to_print = final_map[(i, j)][row]
            strr += row_to_print
        no_gap_map.append(strr)

for rotation in all_rotations(no_gap_map):
    # for i in rotation:
    #     print(i)
    # print()
    count_hs = 0
    count_hs += "..................#.".count("#")
    count_hs += "#....##....##....###".count("#")
    count_hs += ".#..#..#..#..#..#...".count("#")
    found_dragons = 0

    for i in range(len(rotation) - 3):

        d_1 = rotation[i]
        d_2 = rotation[i + 1]
        d_3 = rotation[i + 2]

        first = re.search(r"..................#.", d_1)
        second = re.search(r"#....##....##....###", d_2)
        third = re.search(r".#..#..#..#..#..#...", d_3)

        if first:
            if second:
                if third:
                    first_i = re.search(r"..................#.", d_1).start()
                    second_i = re.search(r"#....##....##....###", d_2).start()
                    third_i = re.search(r".#..#..#..#..#..#...", d_3).start()
                    if first_i == second_i == third_i:
                        found_dragons += 1

    if found_dragons > 0:
        good_rot = rotation

count = 0
for i in good_rot:
    count += i.count("#")

print(count - found_dragons * count_hs)
