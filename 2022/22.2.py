import pathlib
import re

SIDE_LEN = 50

def print_grid(grid, pos, direction):
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if (y,x) == pos:
                if direction == 0:
                    print('\033[93m' + '>' + '\033[0m', end='')
                elif direction == 1:
                    print('\033[93m' + 'V' + '\033[0m', end='')
                elif direction == 2:
                    print('\033[93m' + '<' + '\033[0m', end='')
                elif direction == 3:
                    print('\033[93m' + '^' + '\033[0m', end='')
            else:
                print(c, end='')
        print()
    
    print("---")

path = pathlib.Path('.') / "22.txt"
with open(path, "r") as f:
    grid, moves = f.read().split("\n\n")

def divide_chunks(l, n):
    return [l[i : i + n] for i in range(0, len(l), n)]

moves = divide_chunks(re.findall("\d+|L|R", moves), 2)

grid = [x for x in grid.splitlines()]

height_grid = len(grid)
length_grid = max(len(x) for x in grid)

# augment grid
grid = [x + " " * (length_grid-len(x)) for x in grid]

grid_p2 = divide_chunks(grid, SIDE_LEN)
grid_p2 = [[[c for c in y if c != ' '] for y in x] for x in grid_p2]

new_grid_p2 = []
counter = 0

mappings = set()
for group_of_rows in grid_p2:
    if len(group_of_rows[0]) > SIDE_LEN:
        # i have to split into chunks
        foo = [divide_chunks(x, SIDE_LEN) for x in group_of_rows]
        
        foo = [(counter+i+1, list(x)) for i, x in enumerate(zip(*foo))] # transpose!
        new_grid_p2 += foo
        counter += len(foo)
        pass
    else:
        new_grid_p2.append((counter+1, group_of_rows))
        counter += 1

grids = new_grid_p2

# from now on, a position is (n_grid, (x,y))
starting_point = (1, (0,0))

curr_pos = starting_point


directions = {
    'UP' : (-1,0),
    'RIGHT': (0,1),
    'DOWN' : (1, 0),
    'LEFT': (0,-1)
}

curr_direction = 0
curr_grid = grids[0]

directions_array = ['RIGHT', 'DOWN', 'LEFT', 'UP']

def move_tuple(curr, move, curr_dir):
    n_grid, (cy, cx) = curr
    my, mx = move
    ny, nx = (cy+my), (cx + mx)

    if ny < 0: # vado sopra
        pass
        if n_grid == 1:
            return (6, (nx, 0)), 0
        if n_grid == 2:
            return (6, (SIDE_LEN-1, nx)), 3
        if n_grid == 3:
            return (1, (SIDE_LEN-1, nx)), 3
        if n_grid == 5:
            return (3, (SIDE_LEN-1, nx)), 3
        if n_grid == 4:
            return (3, (nx, 0)), 0
        if n_grid == 6:
            return (4, (SIDE_LEN-1, nx)), 3

    elif ny > SIDE_LEN-1: # vado giu
        pass
        if n_grid == 1:
            return (3, (0, nx)), 1
        if n_grid == 2:
            return (3, (nx, SIDE_LEN-1)), 2
        if n_grid == 3:
            return (5, (0, nx)), 1
        if n_grid == 5:
            return (6, (nx, SIDE_LEN-1)), 2
        if n_grid == 4:
            return (6, (0, nx)), 1
        if n_grid == 6:
            return (2, (0, nx)), 1

    elif nx < 0 : # vado a sx
        pass
        if n_grid == 1:
            return (4, (SIDE_LEN-1-ny, 0)), 0
        if n_grid == 2:
            return (1, (ny, SIDE_LEN-1)), 2
        if n_grid == 3:
            return (4, (0, ny)), 1
        if n_grid == 5:
            return (4, (ny, SIDE_LEN-1)), 2
        if n_grid == 4:
            return (1, (SIDE_LEN-1-ny, 0)), 0
        if n_grid == 6:
            return (1, (0, ny)) , 1

    elif nx > SIDE_LEN-1 : # vado a dx
        pass
        if n_grid == 1:
            return (2, (ny, 0)), 0
        if n_grid == 2:
            return (5, (SIDE_LEN-1-ny, SIDE_LEN-1)), 2
        if n_grid == 3:
            return (2, (SIDE_LEN-1, ny)), 3
        if n_grid == 5:
            return (2, (SIDE_LEN-1-ny, SIDE_LEN-1)), 2
        if n_grid == 4:
            return (5, (ny, 0)), 0
        if n_grid == 6:
            return (5, (SIDE_LEN-1, ny)), 3
    else:
        return (n_grid, (ny, nx)), curr_dir


for m in moves:
    try:
        steps_to_move, direction = m
    except ValueError: # finita l'istruzione
        steps_to_move = m[0]
        direction_to_print = curr_direction % 4

    steps_to_move = int(steps_to_move)

    for i in range(steps_to_move):
        old_pos = curr_pos
        old_dir = curr_direction
        move = directions[directions_array[curr_direction]]
        curr_pos, curr_direction = move_tuple(curr_pos, move, curr_direction)

        curr_grid, (cy, cx) = curr_pos

        if grids[curr_grid-1][1][cy][cx] == '#':
                curr_pos = old_pos
                curr_direction = old_dir
                # print_grid(grid, curr_pos)
                break

    if direction == 'R':
        curr_direction = ((curr_direction+1) % 4)
    if direction == 'L':
        curr_direction = ((curr_direction-1) % 4)

    # print_grid(grids[curr_grid-1][1], curr_pos[1], curr_direction)


curr_grid, (y, x) = curr_pos

if curr_grid == 1:
    x += 50
if curr_grid == 2:
    x += 100
if curr_grid == 3:
    x += 50
    y += 50
if curr_grid == 4:
    y =+100
if curr_grid == 5:
    x += 50
    y += 100
if curr_grid == 6:
    y += 150

print(1000* (y+1) + 4 * (x+1) + direction_to_print)
