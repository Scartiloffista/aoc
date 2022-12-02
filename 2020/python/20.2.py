import pathlib
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


# valerio = ["123",
#            "456",
#            "789"]
# count = 1
# for i in all_rotations(valerio):
#     print(count)
#     count+=1
#     for j in i:
#         print(j)
#     print("")


def create_sides(tile):
    upside = tile[0]
    downside = tile[-1]
    leftside = "".join([line[0] for line in tile])
    rightside = "".join([line[-1] for line in tile])
    return [upside, downside, leftside, rightside]


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


def find_map_left(previous, previous_n, dict_of_sides, dict_of_tiles):
    u, d, l, r = create_sides(previous)
    # now i shoul find what matches on the left of this!
    for candidate in get_candidates_for_side(l, previous_n, dict_of_sides):
        candidate_map = dict_of_tiles[candidate]
        for rotation in all_rotations(candidate_map):
            c_u, c_d, c_l, c_r = create_sides(rotation)
            if l == c_r:  # match!
                return candidate, rotation


def find_map_down(previous, previous_n, dict_of_sides, dict_of_tiles):
    u, d, l, r = create_sides(previous)
    for candidate in get_candidates_for_side(d, previous_n, dict_of_sides):
        candidate_map = dict_of_tiles[candidate]
        for rotation in all_rotations(candidate_map):
            c_u, c_d, c_l, c_r = create_sides(rotation)
            if d == c_u:  # match!
                return candidate, rotation


def find_map_right(previous, previous_n, dict_of_sides, dict_of_tiles):
    u, d, l, r = create_sides(previous)
    for candidate in get_candidates_for_side(r, previous_n, dict_of_sides):
        candidate_map = dict_of_tiles[candidate]
        for rotation in all_rotations(candidate_map):
            c_u, c_d, c_l, c_r = create_sides(rotation)
            if r == c_l:  # match!
                return candidate, rotation


def find_map_up(previous, previous_n, dict_of_sides, dict_of_tiles):
    u, d, l, r = create_sides(previous)
    for candidate in get_candidates_for_side(u, previous_n, dict_of_sides):
        candidate_map = dict_of_tiles[candidate]
        for rotation in all_rotations(candidate_map):
            c_u, c_d, c_l, c_r = create_sides(rotation)
            if u == c_d:  # match!
                return candidate, rotation


def get_candidates_for_side(s, i, dict_of_sides):
    ## get which tile should i be next to on side s
    candididates = dict_of_sides.get(s, [])
    candididates += dict_of_sides.get(s[::-1], [])
    adj = set(candididates) - set([i])
    return adj


path = pathlib.Path(".").parent / "inputs/20.txt"
with open(path, "r") as f:
    input_tiles_raw = f.read().split("\n\n")

tiles = {}
dict_of_sides = {}

for tile in input_tiles_raw:
    temp = tile.splitlines()
    number = int(temp[0].split(" ")[1][:-1])
    tile = temp[1:]
    tiles[number] = tile
    evaluate_tile(tile, number, dict_of_sides)


final_map = {}

# [3343, 3821, 3677, 3709]
final_map[(0, 0)] = (3709, tiles[3709])

listt = []

for i in range(0, 12):
    for j in range(0, 12):
        if i == j == 0:
            continue
        elif j == 0:
            previous_n, previous_map = final_map.get((i - 1, j))
            final_map[(i, j)] = find_map_down(
                previous_map, previous_n, dict_of_sides, tiles
            )
            listt.append(previous_n)
        else:
            previous_n, previous_map = final_map.get((i, j - 1))
            final_map[(i, j)] = find_map_left(
                previous_map, previous_n, dict_of_sides, tiles
            )
            listt.append(previous_n)

sett = set(listt)
# printing!
print("     ", end="")
print("1234567890" * 12)
count = 1
for i in range(0, 12):
    # first row!
    # devo prima stampare le prime righe di ognuno di questi item, poi le seconde righe, etc
    for row in range(0, 10):
        print(f"({count%10}): ", end="")
        count += 1
        for j in reversed(range(0, 12)):
            row_to_print = final_map[(i, j)][1][row]
            print(row_to_print, end="")
        print("")
    # print("")


def remove_gaps(mapp):
    mappp = mapp[1:-1]
    new_map = []
    for line in mappp:
        new_map.append(line[1:-1])
    return new_map


for k, v in final_map.items():
    final_map[k] = remove_gaps(v[1])


# printing!
print("     ", end="")
print("12345678" * 12)
count = 1
for i in range(0, 12):
    # first row!
    # devo prima stampare le prime righe di ognuno di questi item, poi le seconde righe, etc
    for row in range(0, 8):
        print(f"({count%8}): ", end="")
        count += 1
        for j in reversed(range(0, 12)):
            row_to_print = final_map[(i, j)][row]
            print(row_to_print, end="")
        print("")
    # print("")


# saving in list...
final_list = []
for i in range(0, 12):
    # first row!
    # devo prima stampare le prime righe di ognuno di questi item, poi le seconde righe, etc
    for row in range(0, 8):
        strr = ""
        for j in reversed(range(0, 12)):
            row_to_print = final_map[(i, j)][row]
            strr += row_to_print
        final_list.append(strr)

import re


for rotation in all_rotations(final_list):
    count_hs = 0
    count_hs += "..................#.".count("#")
    count_hs += "#....##....##....###".count("#")
    count_hs += ".#..#..#..#..#..#...".count("#")
    found_dragons = 0

    for i in range(len(rotation) - 3):
        # -- ..................#.
        # -- #....##....##....###-
        # -- .#..#..#..#..#..#...

        d_1 = rotation[i]
        d_2 = rotation[i + 1]
        d_3 = rotation[i + 2]

        first = re.search(r"..................#.", rotation[i])
        second = re.search(r"#....##....##....###", rotation[i + 1])
        third = re.search(r".#..#..#..#..#..#...", rotation[i + 2])

        if first:
            if second:
                if third:
                    first_i = re.search(r"..................#.", rotation[i]).start()
                    second_i = re.search(
                        r"#....##....##....###", rotation[i + 1]
                    ).start()
                    third_i = re.search(
                        r".#..#..#..#..#..#...", rotation[i + 2]
                    ).start()
                    if first_i == second_i == third_i:
                        found_dragons += 1
    if found_dragons > 0:
        good_rot = rotation

count = 0
for i in good_rot:
    count += i.count("#")

print(count - found_dragons * count_hs)