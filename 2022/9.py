import pathlib
from typing import Tuple

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

from collections import deque
visited = deque([(0,0)])

def is_near(pos_T: Tuple[int,int], pos_H: Tuple[int,int]):
    Tx, Ty = pos_T
    Hx, Hy = pos_H
    if abs(Tx - Hx) > 1 or abs(Ty-Hy) > 1:
        return False
    else:
        return True

pos_H = (0,0)
pos_T = (0,0)


# is_near((0,2), (0,0))

for instr in instructions:
    direction, steps = instr
    move = moves[direction]

    for _ in range(steps):
        old_pos_H = pos_H
        pos_H = tuple(map(sum,zip(pos_H, move)))
        if not is_near(pos_T, pos_H):
            pos_T = old_pos_H
            visited.append(pos_T)
        
    #     max_x = max([max([x[0] for x in visited]), pos_T[0], pos_H[0]])
    #     min_x = min([min([x[0] for x in visited]), pos_T[0], pos_H[0]])
    #     max_y = max([max([x[1] for x in visited]), pos_T[1], pos_H[1]])
    #     min_y = min([min([x[1] for x in visited]), pos_T[1], pos_H[1]])
        
    #     # ogni item della griglia e' una riga verticale
    #     # quindi si indicizza con grid[y][x]
    #     grid = []
    #     for i in range(len(range(min_y, max_y+1))):
    #         # for j in range(min_x, max_x+1):
    #         row = ['.' for j in range(len(range(min_x, max_x+1)))]
    #         grid.append(row)

    #     grid[pos_H[1]-min_y][pos_H[0]-min_x] = 'H'
    #     grid[pos_T[1]-min_y][pos_T[0]-min_x] = 'T'
        
    #     for i in grid[::-1]:
    #         print(i)
        
    #     print("-")
    #     pass
    
    # print("--")
    # pass


print(len(set(visited)))
