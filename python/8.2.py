import pathlib
import os

path = pathlib.Path('.').parent / "inputs/8.txt"
with open(path, "r") as f:
    lines = f.read().splitlines()

visited = [False] * len(lines)
flag = True
i = 0
acc = 0
is_changed = False

def evaluate(lines, visited, i, acc, is_changed):
    return_values = []

    if i == len(lines):
        return acc
    if visited[i]:
        return None
    
    
    op, number = lines[i].split(" ")

    if op == "acc":
        number = int(number)
        acc += number
        visited[i] = True
        i+=1

        ret_val = evaluate(lines, visited, i, acc, is_changed)
        return_values.append(ret_val)
    
    if op == "nop":
        if is_changed:
            visited[i] = True
            i+=1
            ret_val = evaluate(lines, visited, i, acc, is_changed)
            return_values.append(ret_val)
        else:
            visited[i] = True
            new_i = i
            new_i +=1
            ret_val = evaluate(lines, visited, new_i, acc, is_changed)
            return_values.append(ret_val)

            ## change to jump
            new_i = i
            new_i += int(number)
            ret_val = evaluate(lines, visited, new_i, acc, True)
            return_values.append(ret_val)

    if op == "jmp":
        if is_changed:
            visited[i] = True
            i += int(number)
            ret_val = evaluate(lines, visited, i, acc, is_changed)
            return_values.append(ret_val)
        else:
            visited[i] = True

            new_i = i
            new_i += int(number)
            ret_val = evaluate(lines, visited, new_i, acc, is_changed)
            return_values.append(ret_val)

            # change to noop
            new_i = i
            new_i += 1
            ret_val = evaluate(lines, visited, new_i, acc, True)
            return_values.append(ret_val)


    return next((x for x in return_values if x is not None), None)


val = evaluate(lines, visited, 0, 0, False)
print(val)

