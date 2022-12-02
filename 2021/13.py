
import pathlib

path = pathlib.Path('.').parent / "12.txt"
with open(path, "r") as f:
    data = f.read()

dots, instrs = data.split("\n\n")
dots, instrs = [[int(y) for y in x.split(",")] for x in dots.split("\n")], instrs.split("\n")

# p1
split_line = instrs[0].split("=")[1]
split_line = int(split_line)

def get_new_pos_x(x, y, value):
    if(x > value):
        return (-1*(x % (0-value)), y)
    else:
        return (x, y)

def get_new_pos_y(x, y, value):
    if(y > value):
        return (x, -1*(y % (0-value)))
    else:
        return (x, y)

new_dots = dots

# p2
splits = [x.split("=") for x in instrs]
splits = [(x.split(" ")[2], y) for x, y in splits]

flag = True

for axis, value in splits:
    value = int(value)
    if axis == "x":
        new_dots = {get_new_pos_x(x,y, value) for x,y in new_dots}
        new_dots = {(x,y) for x,y in new_dots}
    else:
        new_dots = {get_new_pos_y(x,y, value) for x,y in new_dots}
        new_dots = {(x,y) for x,y in new_dots}
    if flag:
        print(len(new_dots))
        flag = False

for y in range(max(p[1] for p in new_dots)+1):
    for x in range(max(p[0] for p in new_dots)+1):

        if (x,y) in new_dots:
            print("#", end="")
        else:
            print(" ", end="")
    print("")
