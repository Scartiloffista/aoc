import pathlib

def divide_chunks(l, n):
    return [l[i : i + n] for i in range(0, len(l), n)]

path = pathlib.Path(".") / "10.txt"
with open(path, "r") as f:
    inputt = f.read().splitlines()

acc = []
cycle_counter = 0
register = 1


to_draw = []
# sprite_pos = (0,1,2)

for _, instr in enumerate(inputt):

    sprite = [register-1 % 40, register % 40, register+1 % 40]
    if cycle_counter % 40 in sprite:
        to_draw += ['#']
    else:
        to_draw += ['.']

    if instr == "noop":
        cycle_counter +=1
    else:
        op, value = instr.split(" ")
        value = int(value)
        cycle_counter += 1
        if cycle_counter % 40 in sprite:
            to_draw += ['#']
        else:
            to_draw += ['.']
        
        register += value
        cycle_counter += 1


    # # p1
    # if instr == "noop":
    #     cycle_counter +=1
    # else:
    #     op, value = instr.split(" ")
    #     value = int(value)
    #     cycle_counter += 1
    #     if cycle_counter+1 in [20,60,100,140,180,220]:
    #         to_append = (cycle_counter+1)*register
    #         print(to_append)
    #         acc.append(to_append)
    #     register += value
    #     cycle_counter += 1

    # if cycle_counter+1 in [20,60,100,140,180,220]:
    #     to_append = (cycle_counter+1)*register
    #     print(to_append)
    #     acc.append(to_append)
    # # print(cycle_counter)

# print(sum(acc))

chunks = divide_chunks(to_draw, 40)

for x in chunks:
    print("".join(x))
