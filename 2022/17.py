import pathlib

path = pathlib.Path('.') / "17.txt"
with open(path, "r") as f:
    moves = f.read().strip()

# moves = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

rounds = 0
ROUNDS_LIMIT = 2022
CHAMBER_WIDTH = 7

pieces = [
    # prima y poi x, prima riga poi colonna
    [(0,0), (0,1), (0,2), (0,3)],
    [(0,1), (1,0), (1,1), (1,2), (2,1)],
    [(0,0), (0,1), (0,2), (1,2), (2,2)],
    [(0,0), (1,0), (2,0), (3,0)],
    [(0,0), (1,0), (0,1), (1,1)]
]


def print_grid(rocks, piece, string_to_print, limit_y = None):

    print(string_to_print)
    grid = get_grid(rocks, piece, limit_y)

    lenn = len(grid)

    for i, row in enumerate(grid):
        print(format(lenn-i, '04d') + " |" + "".join(row))

    print("------------")

def get_grid(rocks, piece, limit_y):
    grid = []

    things_to_draw = rocks.union(piece)
    max_y = max(y for y, _ in things_to_draw)

    if limit_y is None:
        limit_y = -1
    else:
        limit_y = max_y-limit_y

    for y in range(max_y, limit_y, -1):
        row = []

        for x in range(7):
            if (y, x) in rocks:
                row.append('#')
            elif (y, x) in piece:
                row.append('@')
            else:
                row.append('.')
        grid.append(row)
    
    return grid

# set up floor
floor = [(-1, i) for i in range(7)]
rocks = set()
rocks.update(set(floor))

rock_index = 0
i_jet = 0

def get_piece_to_deploy(pieces, rocks, rock_n_i):
    piece = pieces[rock_n_i % 5]
    delta_y = max(y for y, _ in rocks) + 4
    piece_to_deploy = move_piece_by_one(piece, rocks, delta_y, 2)
    return piece_to_deploy

def move_piece_by_one(piece, rocks, y, x):
    limit_x = CHAMBER_WIDTH - 1

    candidates = []
    for unit in piece:
        new_unit = tuple(map(sum,zip(unit, (y,x))))
        _, ux = new_unit
        if ux > limit_x or ux < 0 or new_unit in rocks:
            return piece
        candidates.append(new_unit)
    
    return candidates

cache = {}
new_limit = 1000000000000

for step in range(2022 * 3):

    rock_index = step % 5
    move_index = i_jet % len(moves)
    piece_to_deploy = get_piece_to_deploy(pieces, rocks, rock_index)
    string_to_print = "rocks begin to falling"

    current_top = get_grid(rocks, piece_to_deploy, 20)
    current_height = max(y for y, _ in rocks)

    if cache.get((move_index, rock_index), None) is None:
        cache[(move_index, rock_index)] = current_top, step, current_height
    else:
        saved_shape, saved_step, saved_height = cache[(move_index, rock_index)]

        multiplier , modulo = divmod(new_limit-step, step-saved_step)
        if modulo == 0:
            print(current_height + (current_height-saved_height)*multiplier + 1)
            import sys
            sys.exit()

    flag = False
    while not flag:
        move_index = i_jet % len(moves)

        move = moves[move_index]
        i_jet += 1
        if move == '>':
            string_to_print = "Jet of gas pushes rock right:"
            piece_to_deploy = move_piece_by_one(piece_to_deploy, rocks, 0, 1)
        else:
            string_to_print = "Jet of gas pushes rock left:"
            piece_to_deploy = move_piece_by_one(piece_to_deploy, rocks, 0, -1)
        
        # print_grid(rocks, piece_to_deploy, string_to_print)
        old_piece = piece_to_deploy
        string_to_print = "Rock falls 1 unit:"
        piece_to_deploy = move_piece_by_one(piece_to_deploy, rocks, -1, 0)
        if old_piece == piece_to_deploy: # landed?
            rocks.update(old_piece)
            flag = True
        # print_grid(rocks, piece_to_deploy, string_to_print)

# p1
# print_grid(rocks, piece_to_deploy, "")

# max_rock = max(y for y, x in rocks)
# print(max_rock + 1)
