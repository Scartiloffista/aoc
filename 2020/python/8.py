import pathlib
import os

path = pathlib.Path('.').parent / "inputs/8.txt"
with open(path, "r") as f:
    lines = f.read().splitlines()

visited = [False] * len(lines)
flag = True
i = 0
acc = 0

while flag:

    if visited[i]:
        flag = False
        continue

    op, number = lines[i].split(" ")
    if op == "nop":
        visited[i] = True
        i+=1
        continue

    if op == "acc":
        number = int(number)
        acc += number
        visited[i] = True
        i+=1
        continue

    if op == "jmp":
        visited[i] = True
        i += int(number)
        continue
    
print(acc)