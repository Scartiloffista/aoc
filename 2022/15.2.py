
import pathlib
import re

path = pathlib.Path('.') / "15.txt"
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

list_bsd = []


for x in inputt:
    strr = x.replace("Sensor at ", "").replace(": closest beacon is at ", ", ")
    sx, sy, bx, by = map(lambda x: int(x.split("=")[1]), strr.split(", "))


    beacon = (bx,by)
    sensor = (sx,sy)

    beacons.add(beacon)
    sensors.add(sensor)
    list_bsd.append((beacon, sensor, taxicab_dist(beacon, sensor)))

occupati = set()

RIGA = 2000000

acc = 0


def elaborate(ranges):

    ranges.sort(key=lambda x: x[0])

    i = 0
    while i < len(ranges) -1:

        start, end = ranges[i]
        start1, end1 = ranges[i+1]

        if end >= start1 and end >= end1:
            ranges[i] = [start, end]
            del ranges[i+1]
        elif end >= start1 and end1 >= end:
            ranges[i] = [start, end1]
            del ranges[i+1]
        else:
            i += 1
    return ranges



for r in range(4000000, -1, -1):

    ranges = []



    for b, s, d in list_bsd:

        distanza_riga_sensore = abs(s[1]-r)
        if distanza_riga_sensore <= d: # l'area di sto sensore tozza la riga
            
            min_x_area = max(0, s[0]-(d-distanza_riga_sensore))
            max_x_area = min(s[0]+(d-distanza_riga_sensore), 4000000)


            ranges.append([min_x_area, max_x_area])


    ranges = elaborate(ranges)
    if len(ranges) > 1 or ranges[0] != [0,4000000]:
        print(r)
        print(ranges)
        import sys
        sys.exit(0)
