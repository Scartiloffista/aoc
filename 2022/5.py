import pathlib
import re

path = pathlib.Path(".") / "5.txt"
# path = pathlib.Path('.') / "5.example.txt"
with open(path, "r") as f:
    input_list = f.read().split("\n\n")

def divide_chunks(l, n):
    return [l[i : i + n] for i in range(0, len(l), n)]


# parse everything into a grid
grid = input_list[0].splitlines()
grid, n_columns = grid[:-1], grid[-1].strip()
n_columns = int(n_columns.split("   ")[-1]) # last number is how many columns we have
grid = [[y.strip() for y in divide_chunks(x, 4)] for x in grid] # easier to split every row every 4 chars...

def get_stacks(grid):
    # basically transposing
    stacks = [list() for i in range(0, n_columns)]
    for row in grid:
        for i, x in enumerate(row):
            stacks[i] += [x]

    stacks = [[y for y in x if y != ''][::-1] for x in stacks] # removing empty items and reversing the list
    return stacks

stacks = get_stacks(grid)

# now parse moves
moves = input_list[1].strip().splitlines()

list_moves = []
for x in moves:
    m = re.match(r"move (\d+) from (\d+) to (\d+)", x)
    a, b, c = map(int, m.groups())
    list_moves.append((a, b-1, c-1)) # give me back my 0-starting stuff

for x in list_moves:
    amount, fromm, to = x
    to_move = stacks[fromm][-amount:]
    del stacks[fromm][-amount:]
    stacks[to] += to_move#[::-1] remove comment for p1

for x in stacks:
    print(x[-1].replace("[","").replace("]", ""), end="") # lazyness

print("")
