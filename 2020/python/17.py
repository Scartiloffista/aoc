import pathlib

path = pathlib.Path(".").parent / "inputs/17.txt"
with open(path, "r") as f:
    lines = f.read().splitlines()


def transform_input(lines):#: list[str]):
    positions = dict()
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            positions[(i, j, 0, 0)] = char == "#"
    return positions


mapp = transform_input(lines)


def iterate(mapp):
    new_map = dict()

    min_x = min(x[0] for x in mapp.keys())
    min_y = min(x[1] for x in mapp.keys())
    min_z = min(x[2] for x in mapp.keys())
    min_w = min(x[3] for x in mapp.keys())

    max_x = max(x[0] for x in mapp.keys())
    max_y = max(x[1] for x in mapp.keys())
    max_z = max(x[2] for x in mapp.keys())
    max_w = max(x[3] for x in mapp.keys())

    # iterate over whole grid
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            for z in range(min_z - 1, max_z + 2):
                for w in range(min_w - 1, max_w + 2):
                    # iterate over neighbours
                    active_neigh = 0
                    for x_i in [-1, 0, 1]:
                        for y_i in [-1, 0, 1]:
                            for z_i in [-1, 0, 1]:
                                for w_i in [-1, 0, 1]:
                                    if x_i == y_i == z_i == w_i == 0:
                                        continue
                                    # check if neigh is active
                                    if mapp.get(
                                        (x + x_i, y + y_i, z + z_i, w + w_i), False
                                    ):
                                        active_neigh += 1

                    # check if i should be active
                    currently_active = mapp.get((x, y, z, w), False)
                    if currently_active and 2 <= active_neigh <= 3:
                        new_map[(x, y, z, w)] = True
                    if not currently_active and active_neigh == 3:
                        new_map[(x, y, z, w)] = True

    return new_map


for _ in range(6):
    mapp = iterate(mapp)

# print(sum([1 for x in mapp.values() if x]))
