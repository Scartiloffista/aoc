import itertools
import pathlib

path = pathlib.Path('.').parent / "inputs/1.txt"
with open(path, "r") as f:
    input_list = f.read().splitlines()

list_of_numbers = [int(x) for x in input_list]

permutations = list(itertools.permutations(list_of_numbers, 3))

for x in itertools.permutations(list_of_numbers, 3):
    a, b, c = x
    if(a+b+c == 2020):
        print(a*b*c)
