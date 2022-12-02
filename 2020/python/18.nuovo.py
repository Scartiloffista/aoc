import pathlib

path = pathlib.Path(".").parent / "inputs/18.txt"
with open(path, "r") as f:
    lines = f.read().splitlines()


def eval_my_list(my_list):
    # return my_list
    if isinstance(my_list, str):
        return int(my_list)
    # elif len(my_list) == 1:
    #     return int(my_list[0])
    else:
        first = eval_my_list(my_list[0])
        second = eval_my_list(my_list[2:])
        if my_list[1] == '+':
            return first + second
        else:
            return first * second



def evaluate(line):
    i = 0
    listt = []
    build_item = ""
    while i < len(line):
        if line[i] in "0123456789+*":
            # buildin item
            build_item += line[i]
        elif line[i] == " " and build_item != "":
            # item is finished, restarting
            listt.append(build_item)
            build_item = ""
        elif line[i] == "(":
            # starting new nesting
            new_index, new_element = evaluate(line[i + 1 :])
            i += new_index+1
            listt.append(new_element)
            continue
        elif line[i] == ")":# and build_item != "":
            # finishing nesting
            if build_item != "":
                listt.append(build_item)
            return i+1, listt

        i += 1

    if build_item != "":
        listt.append(build_item)
    return i, listt


sum = 0
for i, line in enumerate(lines):
    _, val = evaluate(line)
    val = eval_my_list(val)
    print(f"({i}): {line} diventa {val}")
    print("")
print(sum)