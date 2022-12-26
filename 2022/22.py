import pathlib
import re

path = pathlib.Path('.') / "22.txt"
with open(path, "r") as f:
    grid, moves = f.read().split("\n\n")

def divide_chunks(l, n):
    return [l[i : i + n] for i in range(0, len(l), n)]


grid = [x for x in grid.splitlines()]

height_grid = len(grid)
length_grid = max(len(x) for x in grid)


def move_tuple(curr, move):
    cy, cx = curr
    my, mx = move
    move = (cy+my) % height_grid, (cx + mx) % length_grid
    return move

    # return tuple(map(sum,zip(curr, move)))

# augment grid
grid = [x + " " * (length_grid-len(x)) for x in grid]

# print("\n".join(grid))

moves = divide_chunks(re.findall("\d+|L|R", moves), 2)

def print_grid(grid, pos):
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if (y,x) == pos:
                print('@', end='')
            else:
                print(c, end='')
        print()
    
    print("---")

starting_point = (0, min(i for i, x in enumerate(grid[0]) if x == '.'))

curr_pos = starting_point

directions_array = ['RIGHT', 'DOWN', 'LEFT', 'UP']
directions = {
    'UP' : (-1,0),
    'RIGHT': (0,1),
    'DOWN' : (1, 0),
    'LEFT': (0,-1)
}

curr_direction = 0

for m in moves:
    try:
        steps_to_move, direction = m
    except ValueError: # finita l'istruzione
        print(directions_array[curr_direction])
        steps_to_move = m[0]
        direction_to_print = curr_direction % 4

    steps_to_move = int(steps_to_move)

    for i in range(steps_to_move):
        # salvo la vecchia, mi muovo
        # se sbatto, resto alla vecchia
        old_pos = curr_pos
        move = directions[directions_array[curr_direction]]
        # print_grid(grid, curr_pos)
        curr_pos, curr_direction = move_tuple(curr_pos, move, grid)
        
        cy, cx = curr_pos


        if grid[curr_pos[0]][curr_pos[1]] == '#':
                curr_pos = old_pos
                # print_grid(grid, curr_pos)
                break
        else:
            # print_grid(grid, curr_pos)
            pass
                
    if direction == 'R':
        curr_direction = ((curr_direction+1) % 4)
    if direction == 'L':
        curr_direction = ((curr_direction-1) % 4)

# print(grid)
# print(moves)


cy, cx = curr_pos
# print(curr_pos)
# print(direction_to_print)

print(1000* (cy+1) + 4 * (cx+1) + direction_to_print)
