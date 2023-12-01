import pathlib
import re
from collections import deque

path = pathlib.Path('.') / "18.txt"
with open(path, "r") as f:
    lines = f.read().splitlines()

# parsing
lava_cubes = set()

for x in lines:
    (a,b,c) = map(int, re.findall("\d+", x))
    lava_cubes.add((a,b,c))

# limit for searching
max_n = max(max(i for i in x) for x in lava_cubes)


def p1(lava_cubes, max_n, bubbles = set()):

    count = 0

    for x in range(0, max_n+1):
        for y in range(0, max_n+1):
            for z in range(0, max_n+1):
                if (x, y, z) in lava_cubes:
                    if (x,y,z+1) not in lava_cubes | bubbles:
                        count += 1
                    if (x,y,z-1) not in lava_cubes | bubbles:
                        count += 1
                    if (x,y+1,z) not in lava_cubes | bubbles:
                        count += 1
                    if (x,y-1,z) not in lava_cubes | bubbles:
                        count += 1
                    if (x+1,y,z) not in lava_cubes | bubbles:
                        count += 1
                    if (x-1,y,z) not in lava_cubes | bubbles:
                        count += 1

    return count


def get_neighbours(cube, cubes):

    def filtering_f(cube):
        x, y, z = cube
        if x < 0 or x > max_n: return False
        if y < 0 or y > max_n: return False
        if z < 0 or z > max_n: return False
        return True

    x, y, z = cube
    sett = {(x,y,z+1),
            (x,y,z-1),
            (x,y+1,z),
            (x,y-1,z),
            (x+1,y,z),
            (x-1,y,z)}
    
    sett = set(filter(filtering_f, sett))
    air_cubes = filter(lambda x: x not in cubes, sett)
    lava_cubes = filter(lambda x: x in cubes, sett)
    to_return_air = set(air_cubes)
    to_return_lava = set(lava_cubes)
    return to_return_air, to_return_lava


def p2(lava_cubes):
    touched_lava_cubes = set()

    starting_point = (0,0,0)
    air_cubes_to_visit = deque()
    air_cubes_to_visit.append(starting_point)
    visited_air_cubes = set()
    
    while len(air_cubes_to_visit) > 0:
        current_cube = air_cubes_to_visit.pop()
        visited_air_cubes.add(current_cube)
        air_cubes_touching, lava_cubes_touching = get_neighbours(current_cube, lava_cubes)

        touched_lava_cubes |= lava_cubes_touching 
        air_cubes_touching = air_cubes_touching - visited_air_cubes

        air_cubes_to_visit.extend(air_cubes_touching)


    bubbles = set()
    for x in range(0, max_n+1):
        for y in range(0, max_n+1):
            for z in range(0, max_n+1):
                if (x, y, z) not in visited_air_cubes | lava_cubes:
                    bubbles.add((x,y,z))
    
    return touched_lava_cubes, bubbles


print(p1(lava_cubes, max_n))
touched_lava, bubbles = p2(lava_cubes)
foo1 = p1(lava_cubes, max_n, bubbles)
print(foo1)

