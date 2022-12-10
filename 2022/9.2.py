import pathlib
from typing import Tuple

def is_near(pos_T: Tuple[int,int], pos_H: Tuple[int,int]):
    Tx, Ty = pos_T
    Hx, Hy = pos_H
    if abs(Tx - Hx) > 1 or abs(Ty-Hy) > 1:
        return False
    else:
        return True

def print_grid(visited, pos_H, pos_Ts):
    max_x = max([max([x[0] for x in visited]), max([x[0] for x in pos_Ts]), pos_H[0]])
    min_x = min([min([x[0] for x in visited]), min([x[0] for x in pos_Ts]), pos_H[0]])
    max_y = max([max([x[1] for x in visited]), max([x[1] for x in pos_Ts]), pos_H[1]])
    min_y = min([min([x[1] for x in visited]), min([x[1] for x in pos_Ts]), pos_H[1]])
        
        # ogni item della griglia e' una riga verticale
        # quindi si indicizza con grid[y][x]
    grid = []
    for i in range(len(range(min_y, max_y+1))):
            # for j in range(min_x, max_x+1):
        row = ['.' for j in range(len(range(min_x, max_x+1)))]
        grid.append(row)

    for i, x in enumerate(pos_Ts):
        grid[x[1]-min_y][x[0]-min_x] = str(i+1)

    grid[pos_H[1]-min_y][pos_H[0]-min_x] = 'H'
        
        
    for i in grid[::-1]:
        print(i)
    print("--")
    pass


# path = pathlib.Path(".") / "9.example2.txt"
path = pathlib.Path(".") / "9.txt"
with open(path, "r") as f:
    instructions = [x.split(" ") for x in f.read().splitlines()]
    instructions = [(a,int(b)) for a, b in instructions]

moves = {
    'U' : (0, 1),
    'D' : (0, -1),
    'R' : (1, 0),
    'L' : (-1, 0)
}

visited = {(0,0)}

pos_H = (0,0)
pos_Ts = [(0,0)] * 9

def move_knot(curr, prev):
    cx, cy = curr
    px, py = prev

    if cx != px and cy != py: # different column and row
        foox = 1 if (px > cx) else -1
        fooy = 1 if(py > cy) else -1
        return (cx + foox, cy + fooy)
    elif cx == px: # same column, moving the row
        foo = 1 if(py > cy) else -1
        return (cx, cy + foo)
    else: # same row
        foo = 1 if (px > cx) else -1
        return (cx + foo, cy)




for instr in instructions:
    direction, steps = instr
    move = moves[direction]

    for ii in range(steps):
        old_pos_H = pos_H
        # old_pos_Ts = copy.copy(pos_Ts)
        pos_H = tuple(map(sum,zip(pos_H, move)))

        next_move_for_knots = (0,0)

        if not is_near(pos_Ts[0], pos_H):
            # old_pos = pos_Ts[0]
            # pos_Ts[0] = old_pos_H
            # next_move_for_knots = tuple(map(lambda i, j: i - j, pos_Ts[0], old_pos))
            pos_Ts[0] = move_knot(pos_Ts[0], pos_H)

        for i in range(len(pos_Ts)):
            if i > 0:
                # comparo i con i-1
                curr = pos_Ts[i]
                prev = pos_Ts[i-1]

                if not is_near(curr, prev):
                    # old_pos = pos_Ts[i]
                    # pos_Ts[i] = tuple(map(sum,zip(pos_Ts[i], next_move_for_knots)))
                    # next_move_for_knots = tuple(map(lambda i, j: i - j, pos_Ts[i], old_pos))
                    pos_Ts[i] = move_knot(curr, prev)
                
                if i == 8:
                    visited.add(curr)
            pass
        
        pass

    # print_grid(visited, pos_H, pos_Ts)

print(len(set(visited)))
