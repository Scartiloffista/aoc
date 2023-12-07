import pathlib
import re

# p1
def check_symbols_around_coords(x, y, symbols):
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if (i, j) in symbols.keys():
                return True
    return False

path = pathlib.Path('.') / "3.txt"
with open(path, "r") as f:
    input_list = f.read().strip().splitlines()

maps_symbols = {}
list_numbers = []

for i, line in enumerate(input_list):
    for j, char in enumerate(line):
        if char != "." and not char.isdigit():
            maps_symbols[(i, j)] = char

for i, line in enumerate(input_list):
    numbers_in_line = re.finditer(r'\d+', line)
    for match in numbers_in_line:
        number = int(match.group())
        start, end = match.start(), match.end()
        is_around = False
        for j in range(start, end):
            is_around_this_coord = check_symbols_around_coords(i, j, maps_symbols)
            is_around = is_around or is_around_this_coord
        if is_around:
            list_numbers.append(number)

print(sum(list_numbers))

#p2

gear_symbols = set()

def check_gears(x, y, gears):
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if (i, j) in gears:
                return (i, j)
    return None

for i, line in enumerate(input_list):
    for j, char in enumerate(line):
        if char == '*':
            gear_symbols.add((i, j))

gear_map = {}

for i, line in enumerate(input_list):
    numbers_in_line = re.finditer(r'\d+', line)
    for match in numbers_in_line:
        number = int(match.group())
        start, end = match.start(), match.end()
        for j in range(start, end):
            is_around_this_coord = check_gears(i, j, gear_symbols)
            
            if is_around_this_coord:
                listt = gear_map.get(is_around_this_coord, [])
                listt.append(number)
                gear_map[is_around_this_coord] = listt
                break

list_numbers_p2 = []
for key, value in gear_map.items():
    if len(value) == 2:
        list_numbers_p2.append(value[0] * value[1])

print(sum(list_numbers_p2))
