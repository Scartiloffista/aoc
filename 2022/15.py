
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

for b, s, d in list_bsd:

    candidato = (s[0], RIGA) # controllo sulla riga ma stessa colonna del sensore

    distanza_riga_sensore =  taxicab_dist(candidato, s)
    if distanza_riga_sensore <= d: # l'area di sto sensore tozza la riga
        
        min_x_area = s[0]-(d-distanza_riga_sensore)
        max_x_area = s[0]+(d-distanza_riga_sensore)

        numero_cosi = (d-distanza_riga_sensore)*2+1

        for x in range(min_x_area, max_x_area+1):
            occupati.add((x,RIGA))
        
        # pass
        # for sx, sy in sensors:
        #     if sy == RIGA and min_x_area <= sx <= max_x_area:
        #         numero_cosi -= 1

        # for sx, sy in beacons:
        #     if sy == RIGA and min_x_area <= sx <= max_x_area:
        #         numero_cosi -= 1


        # acc += numero_cosi

# print(get_grid(sensors, beacons, occupati))
print(len(occupati-beacons))

# print(acc)

# foo = [check_if_touches(b,s,d) for b, s, d in list_bsd]



# print(list_bsd)



# max_distance = max(taxicab_dist(b,s) for b, s, _ in list_bsd)

# pass
# max_x = max(x[0] for x in sensors.union(beacons))
# # max_y = max(x[1] for x in sensors.union(beacons))
# min_x = min(x[0] for x in sensors.union(beacons))
# # min_y = min(x[1] for x in sensors.union(beacons))

# RIGA = 2000000

# candidates = set()

# tuttelecose = sensors.union(beacons)

# for x in range(min_x, max_x+1):
#     candidate = (x, RIGA)


#     for _, s, d in list_bsd:
#         if taxicab_dist(candidate, s) <= d and candidate not in tuttelecose:
#             candidates.add(candidate)

# print(len(candidates))


# print(max_distance)

# print(get_grid(sensors, beacons))

# foo = mark_occupied((8,7), (2,10), taxicab_dist((8,7), (2,10)))

# print(get_grid(sensors, beacons, foo))

# occupied = set()

# print(get_grid(sensors, beacons, set()))

# print("")
# print("---")
# print("")

# foo = mark_occupied((8,7), (2,10), taxicab_dist((8,7), (2,10)))

# print(get_grid(sensors, beacons, foo))

# print("")
# print("---")
# print("")

# for beacon, sensor in list_bs:
#     distance = taxicab_dist(sensor, beacon)
#     occupied.update(mark_occupied(sensor, beacon, distance))

# print(get_grid(sensors, beacons, occupied))


# # foo1 = len([1 for (_,y) in ((occupied - beacons)) if y==10])
# foo1 = len([1 for (_,y) in ((occupied - beacons)) if y==2000000])
# print(foo1)
