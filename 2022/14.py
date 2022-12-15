import pathlib
import sys

path = pathlib.Path('.') / "14.txt"
with open(path, "r") as f:
    inputt = f.read().strip().splitlines()

def get_grid(rocks, sands):

    grid = []

    min_rock_x = min(x[0] for x in rocks.union(sands))
    max_rock_x = max(x[0] for x in rocks.union(sands))
    max_rock_y = max(x[1] for x in rocks.union(sands))

    for y in range(0, max_rock_y+1):
        row = []
        for x in range(min_rock_x, max_rock_x+1):
            if (x,y) in rocks:
                row.append('#')
            elif (x,y) in sands:
                row.append('o')
            else:
                row.append('.')
        grid.append(row)

    grid = [str(i) + " " + "".join(x) for i, x in enumerate(grid)]
    return "\n".join(grid)

def add_tuples(a,b):
    return tuple(map(sum, zip(a, b)))


rocks_paths = [[tuple(map(int,y.split(","))) for y in x.strip().split(" -> ")] for x in inputt]

rocks = set()

for rp in rocks_paths:
    for a, b in zip(rp[0:], rp[1:]):
        if a[0] == b[0]: # same x
            maxx, minn = max([a[1], b[1]]), min([a[1], b[1]])
            rocks_to_draw = [(a[0], x) for x in range(minn, maxx+1)]
        else: # same y
            maxx, minn = max([a[0], b[0]]), min([a[0], b[0]])
            rocks_to_draw = [(x, a[1]) for x in range(minn, maxx+1)]
        
        rocks.update(set(rocks_to_draw))
    # print(rocks_to_draw)


sands = set()
unit = 0
source = (500,0)

limit = max(x[1] for x in rocks)

while True:
    
    unit_pos = source
    unit_is_stopped = False
    
    while not unit_is_stopped:
        # p1
        # if(unit_pos[1] == limit):
        #     print(unit)
        #     sys.exit()

        if(unit_pos[1] == limit+1):
            sands.add(unit_pos)
            unit_is_stopped = True
            unit += 1
            

        below = add_tuples(unit_pos, (0,1))
        below_left = add_tuples(unit_pos, (-1,1))
        below_right = add_tuples(unit_pos, (1,1))

        if (below not in rocks) and (below not in sands):
            unit_pos = below
        elif (below_left not in rocks) and (below_left not in sands):
            unit_pos = below_left
        elif (below_right not in rocks) and (below_right not in sands):
            unit_pos = below_right
        else: # mi fermo qua
            sands.add(unit_pos)
            unit_is_stopped = True
            unit += 1

        if(unit_pos == (500, 0)):
            print(unit)
            sys.exit()
    
    # print(get_grid(rocks, sands))

# print(rocks_paths)
