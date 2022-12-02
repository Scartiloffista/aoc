import pathlib

path = pathlib.Path('.') / "1.txt"
with open(path, "r") as f:
    input_list = f.read().split("\n\n") 

calories = sorted([sum(int(y) for y in x.splitlines()) for x in input_list])

print(calories[-1])
print(sum(calories[-3:]))
