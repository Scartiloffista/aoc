
import pathlib
import re

path = pathlib.Path('.') / "15.example.txt"
with open(path, "r") as f:
    inputt = f.read().strip().splitlines()

def add_tuples(a,b):
    return tuple(map(sum, zip(a, b)))

def get_grid(sensors, beacons, occupied):

    grid = []

    max_x = max(x[0] for x in sensors.union(beacons, occupied))
    max_y = max(x[1] for x in sensors.union(beacons, occupied))
    min_x = min(x[0] for x in sensors.union(beacons, occupied))
    min_y = min(x[1] for x in sensors.union(beacons, occupied))


    for y in range(min_y, max_y+1):
        row = []
        for x in range(min_x, max_x+1):
            if (x,y) in sensors:
                row.append('S')
            elif (x,y) in beacons:
                row.append('B')
            elif (x,y) in occupied:
                row.append('#')
            else:
                row.append('.')
        
        id = format(y, '03d')

        grid.append([id] + [" "] +row)

    grid = ["".join(x) for x in grid]
    return "\n".join(grid)

def taxicab_dist(a,b):

    ax, ay = a
    bx, by = b
    return abs(ax - bx) + abs(ay - by)
    
def mark_occupied(sensor, beacon, distance):

    occupied = set()

    for x in range(-distance, distance+1):
        for y in range(-distance, distance+1):
            candidate = add_tuples(sensor, (x,y))
            if taxicab_dist(candidate, sensor) <= distance:
                occupied.add(candidate)

    return occupied




beacons = set()
sensors = set()

list_bs = []


for x in inputt:
    strr = x.replace("Sensor at ", "").replace(": closest beacon is at ", ", ")
    sx, sy, bx, by = map(lambda x: int(x.split("=")[1]), strr.split(", "))

    beacons.add((bx,by))
    sensors.add((sx,sy))
    list_bs.append(((bx,by), (sx,sy)))

# print(get_grid(sensors, beacons))

# foo = mark_occupied((8,7), (2,10), taxicab_dist((8,7), (2,10)))

# print(get_grid(sensors, beacons, foo))

occupied = set()

print(get_grid(sensors, beacons, set()))

for sensor, beacon in list_bs:
    distance = taxicab_dist(sensor, beacon)
    occupied.update(mark_occupied(sensor, beacon, distance))

print(get_grid(sensors, beacons, occupied))

